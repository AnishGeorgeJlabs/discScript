import csv

import pymysql

from var import v_color, v_others
from souper import get_data


def find_parent(c):
    """ Find the parent color for the given color """
    sub = c.strip()
    for k, v in v_color.co_map:
        if sub in v:
            return k


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
        db.execute("SELECT * FROM `Brick` WHERE `Name` = '" + brick + "'")
        n_bricks = list(db)
        # for x in db:
        #     n_bricks.append(x)
        if n_bricks[0][1] < product['n_images']:  # checks the no. of pics with the compliance db.todo, check the index
            record_error("Error in number of images",
                         "site: %i, actual: %s" % (product['n_images'], str(n_bricks[0][1])))

        # ------ CHK 2, Grinding the Model stats ------
        model_stats = specs.get('model stats')

        # --------- CHK 2.1, Size check ---------------

        if len(product['sizes']) > 1 and not product['has_size_chart']:
            record_error("Size Chart Absent", "%i sizes available" % len(product['sizes']))
        elif len(product['sizes']) == 1 and product['sizes'][0] in v_others.dumb_sizes and \
                product['has_size_chart']:
            record_error("Size Chart present with Free size/Standard/Regular")

        desc_sizes = None  # Size specified if any in model stats
        if model_stats and 'size' in model_stats:
            halves = model_stats.split('size')
            desc_sizes = list({
                halves[0].split(" ")[-1].strip(" ."),
                halves[1].split(" ")[0].strip(" .")})

            '''
            # If we have a size array, todo, debatable
            if len(product['sizes']) > 1 and \
                any(x in v_others.dumb_sizes for x in desc_sizes):
                record_error("Free/Standard/Regular mentioned as size for model")
            '''
            # That should do the trick
            if len(product['sizes']) > 0 and \
                    all(x not in product['sizes'] for x in desc_sizes):
                record_error("Size worn by model not available for selection")
            elif all(x not in v_others.dumb_sizes for x in desc_sizes):
                record_error("Size worn by model is unknown")

    except:
        pass
    finally:
        if db:
            db.close()
        if dba:
            dba.close()


'''
def testFunc():
    try:
        a = "Yohoo"
        return
    except:
        pass
    finally:
        print "That's right, we did it"

if __name__ == "__main__":
    testFunc()
'''
