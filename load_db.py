import csv

import pymysql

cnx = pymysql.connect(
    host='localhost',
    user='root',
    db='descrepancy',
    passwd='jlabs11'
)

cnx.autocommit(False)
cursor = cnx.cursor()
stm = """ INSERT INTO urls VALUES (%s, %s, %s, %s, %s, %s); """

with open('database/cor_urls.csv', 'r') as cfile:
    reader = csv.reader(cfile)
    count = 0
    try:
        for row in reader:
            cursor.execute(stm, (row[0], row[1], row[2], row[3], row[4], row[10]))
            count += 1
            print "Total: [%i]" % count
    except Exception:
        raise
        print stm
    cnx.commit()
    print "Done entry"
cursor.close()
cnx.close()
