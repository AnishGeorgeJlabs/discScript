import csv

import re
import pymysql
from var import v_color, v_others, v_adv
from souper import get_data

use_db = False


def find_parent(c):
    """ Find the parent color for the given color """
    sub = c.strip()
    for k, v in v_color.co_map:
        if sub in v:
            return k


def split_para(p):
    """
    :param p: Paragraph
    :return: A list of words
    """
    return [
        word.strip(" .")
        for word in p.replace(',', ' ').split(' ')
        if word
        ]


def clean_para(p):
    freg = re.compile(r'\W+')
    return freg.sub(" ", p)


def extract_colors(desc):
    # step 1, find any of the colors directly in desc
    f_colors = []
    ndesc = desc
    for color in v_color.complete:
        if re.search(r"\b%s\b" % color, ndesc, re.IGNORECASE):
            f_colors.append(color)
            ndesc = ndesc.replace(color, "")

    # step 3, find the previous 3 words
    f_color_dic = {}
    for color in f_colors:
        f_color_dic[color] = split_para(desc.split(color)[0])[-3:]

    # step 4, remove anything that is an auxilary teaming thingy
    for k, v in f_color_dic.items():
        if "with" in v and any(key in v for key in ['team', 'pair', 'club', 'wear', 'style', 'combine']):
            f_color_dic.pop(k)

    return [c.replace("-", " ") for c in f_color_dic.keys()]


'''
if __name__ == '__main__':
    p1 = "Get these brown pants. Team it with white shirt".lower()
    p2 = "These navy blue trousers are worth the buck".lower()
    p3 = "These navy blue trousers are the bang. With a blue crease".lower()
    print "Colors: ", extract_colors(p3)
    '''


def main_algorithm(url, prod_id="", brick="", category="", sku="", brand="", mrp="", item_type=""):
    """
    Main algorithm, a mess it is
    :param url: the product url
    :param prod_id:
    :param brick:
    :param category:
    :param sku:
    :param brand:
    :param mrp:
    :param item_type:
    :return:
    """
    errors = []  # the list of discrepancies we recording
    try:
        # DB stuff
        if use_db:
            dba = pymysql.connect(host="localhost", user="root", passwd="", db="discrepancy")  # discrpancy
            db = dba.cursor()
        # --------------------

        product, soup = get_data(url)
        specs = product.get("specs")

        if False:  # todo, check if the link is not alive
            with open('skipped_links.csv', 'a+') as cfile:
                writer = csv.writer(cfile)
                writer.writerow([url])
                return

        def record_error(error, additional=""):
            errors.append(error)
            print "> %s: %s -- %s" % (sku, error, additional)

        # ------ CHK 1, number of pics ----------------
        if use_db:
            db.execute("SELECT * FROM `Brick` WHERE `Name` = '" + brick + "'")
            n_bricks = list(db)
            # for x in db:
            #     n_bricks.append(x)
            if n_bricks[0][1] < product[
                'n_images']:  # checks the no. of pics with the compliance db.todo, check the index
                record_error("Error in number of images",
                             "site: %i, actual: %s" % (product['n_images'], str(n_bricks[0][1])))

        # ------ CHK 2, Size chart and selections ------
        if len(product['sizes']) > 1 and not product['has_size_chart']:
            record_error("Size Chart Absent", "%i sizes available" % len(product['sizes']))
        elif len(product['sizes']) == 1 and product['sizes'][0] in v_others.dumb_sizes and \
                product['has_size_chart']:
            record_error("Size Chart present with Free size/Standard/Regular")

        # ------ CHK 3, Grinding the Model stats ---------------------------------------------------
        model_data = product.get('model_data')
        if model_data:
            # --------- CHK 3.1, Size check ---------------
            if 'size' in model_data:
                desc_sizes = model_data['size']
                if all(x not in product['sizes'] for x in desc_sizes):
                    if len(product['sizes']) > 0:
                        record_error("Size worn by model not available for selection",
                                     "%s, %s" % (str(desc_sizes[0]), str(desc_sizes[-1])))
                    elif all(x not in v_others.dumb_sizes for x in desc_sizes):
                        record_error("Size worn by model is unknown")

            # --------- CHK 3.2, Body measurements --------
            if "hips" in model_data:
                record_error("Hips mentioned in Model stats")

            for key in ["chest", "waist", "bust", "hip", "hips"]:
                if key in model_data:
                    val = model_data[key][:2]
                    if not unicode(val).isnumeric():
                        record_error("Invalid %s size" % key, str(val))

            if "height" in model_data and model_data['height'] not in v_others.height_range:
                record_error("Invalid height", str(model_data['height']))

        # ------- CHK 4, Extracting data from description ------------------------------------------
        desc_data = {}
        color = {}
        if not product.get('desc'):
            record_error("Discription Not Present")
        else:
            # ------ CHK 4.1, Colors --------------------------
            color['description'] = extract_colors(product['desc'])  # Keep this separate
            # ------ CHK 4.2, Rest of the fields --------------
            for key in v_adv.spec_fields:
                desc_data[key] = []
                for i in v_adv.data_map[key]:
                    if re.search(r'\b%s\b' % i, product['desc'], re.IGNORECASE):
                        desc_data[key].append(i)
            desc_data['fit'] = [x.replace("fit", "").replace('-', ' ').strip() for x in desc_data['fit']]

        color['name'] = extract_colors(product['name'].lower())

        # ------ CHK 5, Basic Checks of description against specs ----------------------------------
        for k, v in desc_data.items():
            for item in v:
                if item not in product['specs'].get(k, ""):
                    record_error("%s details mismatch in description" % k,
                                 "desc: %s, specs: %s" % (str(v), str(product['specs'].get(k, ''))))

        # ------ CHK 6, Segment - category specific checks -----------------------------------------
        subcat = product.get("subcat", "")
        if subcat == "watches":
            spec_colors = clean_para(specs.get('strap color', ''))
        elif subcat == "sunglasses":
            frame = specs.get('frame color', '')
            lens = specs.get('lens color', '')

            spec_colors = clean_para((frame + " " + lens).strip())
            for key in ['name', 'description']:
                if any(not re.search(r"\b%s\b" % x, spec_colors) for x in color[key]):
                    record_error("Colors in %s not matching with specs" % key)
        else:
            spec_colors = specs.get('color', '')

        if spec_colors == "":
            record_error("No Color")
        elif any(x in spec_colors for x in ['na', 'n/a']):
            record_error("Color N/A error")

        # ------ CHK 7, random stuff ---------------------------------------------------------------
        is_bag = brick.lower() in v_others.bag_list
        if (category.lower() == "apparel" or is_bag) and not model_data:
            record_error("Model Vitals Absent")
        elif is_bag and model_data and "height" not in model_data:
            record_error("Incomplete Model Vitals")

        # ------ CHK 8, Material check -------------------------------------------------------------
        material = specs.get("material")  # ASSUMPTION, gives a single material
        if material:
            pat = re.compile(r"(\d+|%)")
            material_details = v_others.data_map.get(category.lower(), '')

            desc_materials = set()
            for md in material_details:
                if re.search(r"\b%s\b" % md, product.get('desc', '')):
                    md = pat.sub('', md)
                    desc_materials.add(md)

            if len(desc_materials):
                c_material = pat.sub('', material)
                if c_material not in desc_materials:
                    record_error("Mismatch in material",
                                 "specs: %s, description: %s" % (str(material), str(desc_materials)))

        # ------ CHK 9, Assorted and multi ---------------------------------------------------------
        def check_assorted_multi(a,b):
            if a in product['name']:
                if b in spec_colors:
                    record_error("%s is mentioned in color" % b.title())
                elif a not in spec_colors and len(spec_colors):
                    record_error("%s is missing in color" % a.title())
                return True
            else:
                return False

        if check_assorted_multi("assorted", "multi") and check_assorted_multi("multi", "assorted"):
            record_error("Both of assorted and multi are mentioned in name")






    except Exception, e:
        raise
        print "Received exception ", e
    finally:
        if use_db:
            if db:
                db.close()
            if dba:
                dba.close()
        print "Done, errors: "
        print errors


'''
def testFunc():
    try:
        a = "Yohoo"
        return
    except:
        pass
    finally:
        print "That's right, we did it"
'''
if __name__ == "__main__":
    from souper import url_sunglass, url_multi

    main_algorithm(url_multi, sku="TestSub 1")
