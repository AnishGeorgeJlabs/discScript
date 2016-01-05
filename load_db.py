import csv

import pymysql

cnx = pymysql.connect(
    host='localhost',
    user='root',
    db='desc_local',
    passwd='jlabs11'
)

cnx.autocommit(False)
cursor = cnx.cursor()
stm = """ INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s); """
stma = """
INSERT INTO data (sku, brand, category, class, brick, price, item_id, url)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""

with open('database/cor_urls.csv', 'r') as cfile:
    reader = csv.reader(cfile)
    count = 0
    try:
        for row in reader:
            row = map(lambda k: None if k == "NULL" or k == "" else k, row)
            #cursor.execute(stm, (row[0], row[1], row[2], row[3], row[4], row[10]))
            cursor.execute(stma, (
                row[0], row[1], row[2], row[3], row[4],
                int(float(row[8])),
                row[9], row[10]
            ))
            count += 1
            print "Total: [%i]" % count
    except Exception:
        raise
    cnx.commit()
    print "Done entry"
cursor.close()
cnx.close()
