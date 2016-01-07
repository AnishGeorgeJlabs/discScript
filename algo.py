import csv
import re

from var import v_color, v_others, v_adv, db_fix
from souper import get_data
from functions import split_para_into_sentences, has_item_value


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
        word
        for word in re.split('\W+', p)
        if word
        ]


def find_nearby(word, para):
    """
    Finds the nearby words of a any given word in a para, the immediate left and right only
    :param word:
    :param para:
    :return:
    """

    def helper(subpara):
        sp = re.split(word, subpara, maxsplit=1)
        if len(sp) == 1:
            return []
        else:
            splits = [split_para(x) for x in sp]
            s = set()
            if len(splits[0]):
                s.add(splits[0][-1])
            if len(splits[-1]):
                s.add(splits[-1][0])
            return list(s) + helper(sp[1])

    return helper(para)




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
        print "pre"
        product, soup = get_data(url)
        specs = product.get("specs")
        print "after"

        if False:  # todo, check if the link is not alive
            with open('skipped_links.csv', 'a+') as cfile:
                writer = csv.writer(cfile)
                writer.writerow([url])
                return

        def record_error(error_code, help_text="", details=None):
            errors.append({
                "code": int(error_code),
                "details": details
            })
            # print "> %s: [%i] %s -- %s" % (sku, error_code, help_text, details)

        # ------ CHK 1, number of pics ----------------
        print "check 1"
        r_images = db_fix.brick_image_map.get(brick)
        if r_images and r_images < product['n_images']:
            record_error(33,
                         help_text="Error in number of images",
                         details="brick: %s, shown: %i, required: %i" % (
                         brick, product['n_images'], db_fix.brick_image_map.get(brick, 0)))

        # ------ CHK 2, Size chart and selections ------
        print "check 2"
        if len(product['sizes']) > 1 and not product['has_size_chart']:
            record_error("Size Chart Absent", "%i sizes available" % len(product['sizes']))
        elif len(product['sizes']) == 1 and product['sizes'][0] in v_others.dumb_sizes and \
                product['has_size_chart']:
            record_error(35, help_text="Size Chart present with Free size/Standard/Regular")

        # ------ CHK 3, Grinding the Model stats ---------------------------------------------------
        # print "check 3"
        model_data = product.get('model_data')
        if model_data:
            # --------- CHK 3.1, Size check ---------------
            if 'size' in model_data:
                desc_sizes = model_data['size']
                if all(x not in product['sizes'] for x in desc_sizes):
                    if len(product['sizes']) > 0:
                        record_error(36, help_text="Size worn by model not available for selection",
                                     details="model has unavailable size of either - %s - or - %s -" % (
                                         str(desc_sizes[0]), str(desc_sizes[-1])))
                    elif all(x not in v_others.dumb_sizes for x in desc_sizes):
                        record_error(37, help_text="Size worn by model is unknown")

            # --------- CHK 3.2, Body measurements --------
            if "hips" in model_data:
                record_error(38, help_text="Hips mentioned in Model stats")

            for key in ["chest", "waist", "bust", "hip", "hips"]:  # have to work on this to get uniform model
                if key in model_data:
                    val = model_data[key][:2]
                    if not unicode(val).isnumeric():
                        record_error(db_fix.vital_errors_map[key], help_text="Invalid %s size" % key,
                                     details='Invalid size: %s' % str(val))

            if "height" in model_data and model_data['height'] not in v_others.height_range:
                record_error(db_fix.vital_errors_map['height'], help_text="Invalid height",
                             details='Invalid size: %s' % str(model_data['height']))

        # ------- CHK 4, Extracting data from description ------------------------------------------
        desc_data = {}
        color = {}
        color['name'] = extract_colors(product['name'].lower())
        if not product.get('desc'):
            record_error(44, help_text="Discription Not Present")
        else:
            # ------ CHK 4.1, Colors --------------------------
            color['description'] = extract_colors(product['desc'])  # Keep this separate, todo change

            desc_split = split_para_into_sentences(product['desc'])

            for key in v_adv.spec_fields:
                if key in specs:
                    # step 1, get all the data from descriptions
                    data = [
                        item for item in v_adv.data_map[key]
                        if any(has_item_value(sentence, item) for sentence in desc_split)
                    ]
                    # step 2, check if the spec item is there in the data, if there then remove it
                    if specs[key] in data:
                        data.pop(data.index(specs[key]))

                    # step 3, filter out tricky words
                    data = filter(lambda w: w not in v_adv.tricky_words, data)

                    if len(data):
                        record_error(45, help_text='%s details mismatch in description' % key,
                                     details='for section: %s, description gives %s while specs give %s' %
                                             (key, str(data), str(specs[key])))

            '''
            # ------ CHK 4.2, Rest of the fields --------------
            for key in v_adv.spec_fields:
                desc_data[key] = []
                for i in v_adv.data_map[key]:
                    if re.search(r'\b%s\b' % i, product['desc'], re.IGNORECASE):
                        if key not in v_adv.tricky_fields or key in find_nearby(i, product['desc']):
                            desc_data[key].append(i)
            desc_data['fit'] = [x.replace("fit", "").replace('-', ' ').strip() for x in desc_data['fit']]
            '''

        '''
        # ------ CHK 5, Basic Checks of description against specs ----------------------------------
        for k, v in desc_data.items():
            for item in v:
                if item not in product['specs'].get(k, ""):
                    record_error(45, help_text="%s details mismatch in description" % k,
                                 details="for section: %s, description gives %s while specs give %s" % (
                                     k, str(v), str(product['specs'].get(k, ''))))

        '''
        # ------ CHK 6, Segment - category specific checks, for color ------------------------------
        subcat = product.get("subcat", "")
        if subcat == "watches":
            spec_color = specs.get('strap color', '')
        elif subcat == "sunglasses":
            frame = specs.get('frame color', '')
            lens = specs.get('lens color', '')

            spec_color = (frame + "," + lens).strip()  # I think this was the intention
        else:
            spec_color = specs.get('color', '')

        if spec_color == "":
            record_error(46, help_text="No Color")
        elif any(x in spec_color for x in ['na', 'n/a']):
            record_error(47, help_text="Color N/A error")

        # ------ CHK 6.1, Assorted and multi --------------------------------------------------------
        # print "check 6"
        def check_assorted_multi(a, b):
            if a in product['name']:
                if b in spec_color:
                    record_error(db_fix.assorted_multi_map[b], help_text="%s is mentioned in color" % b.title())
                elif a not in spec_color and len(spec_color):
                    record_error(db_fix.assorted_multi_miss_map[a], help_text="%s is missing in color" % a.title())
                return True
            else:
                return False

        if check_assorted_multi("assorted", "multi") and check_assorted_multi("multi", "assorted"):
            record_error(50, help_text="Both of assorted and multi are mentioned in name")

        # ------ CHK 6.2, Match colors against name and description --------------------------------
        # print "check 6"
        for key in ['name', 'description']:
            if any(not re.search(r"\b%s\b" % x, spec_color) for x in color.get(key, [])):
                record_error(db_fix.color_match_specs_map[key],
                             help_text="Colors in %s not matching with specs" % key)

        # ------ CHK 6.3, check if the color is available in the list ------------------------------
        if any(c not in v_color.complete for c in spec_color.split(',')):
            record_error(53, help_text="Color not found in list")

        # ------ CHK 7, random stuff ---------------------------------------------------------------
        is_bag = brick.lower() in v_others.bag_list
        if (category.lower() == "apparel" or is_bag) and not model_data:
            record_error(54, help_text="Model Vitals Absent")
        elif is_bag and model_data and "height" not in model_data:
            record_error(55, help_text="Incomplete Model Vitals")

        # ------ CHK 8, Material check -------------------------------------------------------------
        # print "check 8"
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
                    record_error(56, help_text="Mismatch in material",
                                 details="material in specs: %s and in description: %s" % (
                                     str(material), str(desc_materials)))

        # ------ CHK 9, Package contents -----------------------------------------------------------
        # print "check 9"
        numeric_set = ['set of', 'pack of', 'combo of']
        non_numeric_set = ['suit set']
        if any(x in product['desc'] for x in numeric_set + non_numeric_set) and 'package contents' not in specs:
            record_error(57, help_text="Package contents absent")

        for x in numeric_set:
            if x in product['desc']:
                try:
                    contents = int(split_para(product['desc'].split(x)[1])[0])
                    if str(contents) not in specs.get("package contents", ""):
                        raise Exception("not available in specs")
                except:
                    record_error(58, help_text="Error in Package Contents")

        # print 'end'
        return errors
    except Exception, e:
        raise


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
    url_package_1 = "http://www.jabong.com/jaipur-kurti-Multi-Colored-Printed-Cotton-Salwar-Kameez-Dupatta-1790943.html?pos=2"
    url_package_2 = "http://www.jabong.com/sir-michele-Sir-Michele-Ladies-Designer-Anklet-Socks5-Pairs-1851601.html?pos=1"

    from souper import url1, url2, url3, url_multi

    errors = main_algorithm(url1, sku="TestSub 1")
    print errors
