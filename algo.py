import pymysql
from var import v_color
from souper import get_data
import csv

# Find the parent color for the given color
def find_parent(c):
    sub = c.strip()
    for k, v in v_color.co_map:
        if sub in v:
            return k


def main_algorithm( url, prod_id="", brick="", category="", sku="", brand="", mrp="", item_type="" ):
    try:
        # DB stuff
        dba = pymysql.connect(host="localhost", user="root", passwd="", db="discrepancy")  # discrpancy
        db = dba.cursor()
        # --------------------

        product, soup = get_data(url)

        if False:           # todo, check if the link is not alive
            with open('skipped_links.csv', 'a+') as cfile:
                writer = csv.writer(cfile)
                writer.writerow([url])
                return

        errors = []

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