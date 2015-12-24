import csv

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


def extract_colors(desc):
    # step 1, find any of the colors directly in desc
    f_colors = []
    ndesc = desc
    for color in v_color.complete:
        if " %s " % color in ndesc:
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

    return [c.replace(" ", "-") for c in f_color_dic.keys()]


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

        errors = []  # the list of discrepancies we recording

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
        # model_stats = specs.get('model stats')    # not needed as of now
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
        spec_fields = ['closing', 'neck', 'lining', 'fit', 'heelshape', 'sleeves', 'length', 'style']
        desc_data = {}
        if not product.get('desc'):
            record_error("Discription Not Present")
        else:
            # ------ CHK 4.1, Colors --------------------------
            desc_data["color"] = extract_colors(product['desc'])
            # ------ CHK 4.2, Rest of the fields --------------
            for key in spec_fields:
                desc_data[key] = []
                for i in v_adv.data_map[key]:
                    if " %s " % i in product['desc']:
                        desc_data[key].append(i)
            desc_data['fit'] = [x.replace("fit", "").replace('-', ' ').strip() for x in desc_data['fit']]

        color_in_name = extract_colors(product['name'].lower())

        # ------ CHK 5, Basic Checks of description against specs ----------------------------------
        for k, v in desc_data.items():
            for item in v:
                if item not in product['specs'].get(k, ""):
                    record_error("%s details mismatch in description" % k, "desc: %s, specs: %s" % (str(v), str(product['specs'].get(k, ''))))



    except:
        pass
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
    from souper import url1, url2, url3

    main_algorithm(url1, sku="TestSub 1")
