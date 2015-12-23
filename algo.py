from var import v_color
from souper import get_data

# Find the parent color for the given color
def find_parent(c):
    sub = c.strip()
    for k, v in v_color.co_map:
        if sub in v:
            return k


def main_algorithm( url, prod_id="", brick="", category="", sku="", brand="", mrp="", item_type="" ):
    try:
        pass
    except:
        pass