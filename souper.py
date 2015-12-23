from bs4 import BeautifulSoup
import pprint
import requests


def get_data(url):
    """ Get the Product data by scrapping off page
    :param url: The product description page from jabong
    :return: A complete product dictionary
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    def find_by_class(c, tag="span"):
        obj = soup.find(tag, class_=c)
        if obj:
            return obj.string.strip()
        else:
            return None

    res = {
        "name": find_by_class("product-title"),
        "brand": find_by_class("brand"),
        "has_size_chart": bool(soup.find(id="size-block").find("a", class_="help dialogify")),     # todo, recheck
        "desc": find_by_class("prod-disc", "h2"),
        "n_images": len(soup.find("div", class_="product-carousel").find_all("img"))
    }
    spec_list = soup.find("ul", class_="prod-main-wrapper").find_all("li")
    specs = {}
    for item in spec_list:
        if 'authorized-brand' in item.get('class', []):
            continue
        specs[item.label.string.strip().lower()] = item.span.string
    res['specs'] = specs

    return res, soup


if __name__ == "__main__":
    printer = pprint.PrettyPrinter(indent=2)
    url1 = "http://www.jabong.com/phosphorus-Mandarin-collar-oxford-casual-shirt-1570940.html?pos=1"
    url2 = "http://www.jabong.com/park-avenue-Blue-Striped-Slim-Fit-Formal-Shirt-1623073.html?pos=2"
    prod, soup = get_data(url2)
    printer.pprint(prod)
