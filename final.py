import pymysql

import sys

if len(sys.argv) < 3:
    print "Please enter a runcode and console code"
    quit()


# name = {}
# material_details = {}
# count = 1
# ------------------------ checkpoint 0, DB setup ----- Some kind of error reporting I guess ---------------------------
dba = pymysql.connect(host="localhost", user="root", passwd="", db="discrepancy")  # discrpancy
db = dba.cursor()
selq = "SELECT `error_code`,`error_desc` FROM error"
db.execute(selq)
n_error = db.rowcount
'''
codes = {}
for x in db:
    codes[x[1]] = x[0]
'''
codes = dict((x[1], x[0]) for x in db)

db.close()
dba.close()
del db
del dba
# seqer = {}        # keep count of number of errors in database

# We will keep the main algorithm separate for sanity

# ------------------------ checkpoint N, Final work --------------------------------------------------------------------
# TODO, add rest of code