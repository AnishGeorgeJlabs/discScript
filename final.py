from datetime import datetime
from algo import main_algorithm
import pprint

from var import cnx

debug_mode = True

data_stm = "SELECT url, sku, category, brick, brand from data"
if debug_mode:
    data_stm += " LIMIT 1000, 3"
    run_table = "run_test"
    result_table = "result_test"
else:
    run_table = "run"
    result_table = "result"

start_time = datetime.now()  # start time of the run
db = cnx.cursor()
'''
db.execute("INSERT into %s (start_time)" % run_table + " VALUES (%s)", start_time)
run_code = list(db.execute("SELECT LAST_INSERT_ID()"))[0][0]  # the currently generated run code
'''

printer = pprint.PrettyPrinter(indent=2)
db.execute(data_stm)
for row in db:
    errors = main_algorithm(
        url=row[0],
        sku=row[1],
        category=row[2].lower(),
        brick=row[3].lower(),
        brand=row[4]
    )
    printer.pprint({"url": row[0], "errors": errors})
