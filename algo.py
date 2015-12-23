import csv

import pymysql

from var import v_color
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

        # ------ CHK 2, Grinding the description ------
        # --------- CHK 2.1, Size check ---------------

        if len(product['sizes']) > 1 and not product['has_size_chart']:
            record_error("Chart Absent", "%i sizes available" % len(product['sizes']))

        desc_size = None
        if product['desc'] and 'size' in product['desc']:
            desc_size = product['desc'].split('size')[1].strip(" .")

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
