# These are variables which are tied pretty tightly to the database schema so make sure you update if the db changes
from . import cnx
vital_errors_map = {
    "chest": 39,
    "waist": 40,
    "bust": 41,
    "hip": 42, "hips": 42,
    "height": 43
}

assorted_multi_map = {
    "assorted": 48,      # mentioned in the name which is the error
    "multi": 49
}
assorted_multi_miss_map = {
    "assorted": 60,
    "multi": 61
}

color_match_specs_map = {
    "name": 51,          # color in name not matching with specs
    "description": 52
}

db = cnx.cursor()
db.execute("SELECT * from brick")
brick_image_map = dict(db)
