from bs4 import BeautifulSoup
import requests

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    def find_by_itemprop(p, tag="span"):
        obj = soup.find(tag, itemprop=p)
        if obj:
            return obj.string
        else:
            return None
        '''
        '''

    res = {
        "name": find_by_itemprop("name"),
        "brand": find_by_itemprop("brand"),
        "has_size_chart": bool(soup.find(id="size-block")),
        "desc": find_by_itemprop("description", "h2"),
        "images_count": len(soup.find("div", class_="product-carousel").find_all("img"))
    }
    spec_list = soup.find("ul", class_="prod-main-wrapper").find_all("li")
    specs = {}
    for item in spec_list:
        specs[item.label.string.lower()] = item.span.string
    res['specs'] = specs

    return res, soup


if __name__ == "__main__":
    url = "http://www.jabong.com/phosphorus-Mandarin-collar-oxford-casual-shirt-1570940.html?pos=1"
    prod, soup = get_data(url)
    print prod