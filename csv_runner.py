from algo import main_algorithm

import csv
from ftplib import FTP
import pymysql

file_name = 'database/sample_urls.csv'

cnx = pymysql.connect(
    host='localhost',
    user='root',
    db='descrepancy',
    passwd='jlabs11'
)
cnx.autocommit(False)
cursor = cnx.cursor()
stm = "INSERT INTO errors (sku, error) values (%s, %s)"

with open(file_name, 'r') as cfile:
    reader = csv.reader(cfile)

    for row in reader:
        errors = main_algorithm(
            row[10],
            sku=row[0],
            brand=row[1],
            category=row[2],
            brick=row[4]
        )
        if errors and len(errors):
            for error in errors:
                cursor.execute(stm, (row[0], error))
            cnx.commit()

#'''
with open('result.csv', 'w') as wfile:
    writer = csv.writer(wfile)
    cursor.execute("SELECT errors.sku, category, class, brick, url, error FROM errors INNER JOIN urls on urls.sku = errors.sku ")
    writer.writerows(cursor)

ftp = FTP('jabongfeedback.com')
ftp.login('Rahul', 'R@hul@123')
ftp.set_pasv(True)
ftp.cwd("/Desc")
with open('result.csv', 'r') as fl:
    ftp.storlines('STOR descrepancy_result.csv', fl)

ftp.close()
#'''
