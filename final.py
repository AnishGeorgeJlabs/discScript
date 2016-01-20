from datetime import datetime
from algo import main_algorithm
import pprint

from var import cnx

debug_mode = True

data_stm = "SELECT url, sku, category, brick, brand from data"
if debug_mode:
    data_stm += " LIMIT 100, 400"
    run_table = "run_test"
    result_table = "result_test"
else:
    run_table = "run"
    result_table = "result"

start_time = datetime.now()  # start time of the run
db = cnx.cursor()

db.execute("INSERT into %s (start_time)" % run_table + " VALUES (%s)", start_time)
db.execute("SELECT LAST_INSERT_ID()")
run_code = list(db)[0][0]  # the currently generated run code
cnx.commit()
print "GOT run code: ", run_code

printer = pprint.PrettyPrinter(indent=2)
db.execute(data_stm)
data = list(db)
#substm = "INSERT INTO %s (fk_run, fk_sku, fk_error, details)" % result_table + " VALUES "
for row in data:
    errors = main_algorithm(
        url=row[0],
        sku=row[1],
        category=row[2].lower(),
        brick=row[3].lower(),
        brand=row[4]
    )
    printer.pprint({"url": row[0], "errors": errors})
    for error in errors:
        db.execute(
            "INSERT INTO %s (fk_run, fk_sku, fk_error, details)" % result_table +
            " VALUES (%s,%s,%s,%s)",
            (run_code, row[1], error['code'], error['details'])
        )

db.execute(
    "UPDATE %s" % run_table +
    " SET end_time = %s WHERE id_run = %s",
    (datetime.now(), run_code)
)
cnx.commit()
print "DONE"
