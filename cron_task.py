import pymysql
from ftplib import FTP
import csv

cnx = pymysql.connect(
    host='localhost',
    user='root',
    db='descrepancy',
    passwd='jlabs11'
)
cursor = cnx.cursor()
stm = """SELECT errors.sku, category, class, brick, url, error
         FROM errors INNER JOIN urls on urls.sku = errors.sku"""

with open('result_partial.csv', 'w') as wfile:
    writer = csv.writer(wfile)
    cursor.execute(stm)
    writer.writerows(cursor)

ftp = FTP('jabongfeedback.com')
ftp.login('Rahul', 'R@hul@123')
ftp.set_pasv(True)
ftp.cwd("/Desc")
with open('result_partial.csv', 'r') as fl:
    ftp.storlines('STOR descrepancy_cron.csv', fl)

ftp.close()

