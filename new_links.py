from bs4 import BeautifulSoup
import time
import sys
import requests
from string import maketrans
import csv

import pymysql
from image import read_image  # imgtest=>image
from colors import colorname
from var import v_color, v_others, v_adv
import re as regex
import var.v_adv

if len(sys.argv) < 3:
    print "Please enter a runcode and console code"
    quit()

name = {}
material_details = {}
count = 1

# Find the parent color for the given color
def find_parent(c):
    sub = c.strip()
    for k, v in v_color.co_map:
        if sub in v:
            return k

# DB setup  -------------------------------------- Checkpoint 1 --------------------------------------------------------
dba = pymysql.connect(host="localhost", user="root", passwd="", db="discrepancy")  # discrpancy
db = dba.cursor()
selq = "SELECT `error_code`,`error_desc` FROM error"
db.execute(selq)
tnumerror = db.rowcount
j = tnumerror
codes = {}
for x in db:
    report = x
    codes[report[1]] = report[0]
    j = j - 1
db.close()
dba.close()
del db
del dba
# seqer = {} #used to keep count of the number of errors in the database.
j = tnumerror

# Diff function not used so not writing
# ------------------------------------------------ Checkpoint 2 ------------ Copied right now --------------------------

def get_articles(url, prod_id="", brick="", category="", SKUU="", Brandd="", MRP="", ItemType=""):
    try:

        r = requests.get(url)
        html = r.text  # opens the url and fetch HTML
        dba = pymysql.connect(host="localhost", user="root", passwd="", db="discrepancy")  # discrpancy
        db = dba.cursor()
        if 1:
            soup = BeautifulSoup(html, "html5lib")  # opens HTML to be parsed
            p = []
            if soup.find("span", "fs18"):  # checks whether link is live or not
                file = open('skipped_links.csv', 'a+')
                file.write(url)
                file.close()
            else:
                ecode = ""

                # d = enchant.Dict("en_GB","")
                # d = enchant.DictWithPWL("en_GB","testdict.txt")
                # ------------------- Checkpoint, beautiful soup -------------------------------------------------------
                name = soup.find("span", "fs11 c222").string.strip('\t\n ').lower()  # Name alongside Brick
                brand_name = soup.find("span", "brand-name fs22 full-width").string.strip('\t\n ')  # Brand Name
                name_below_brand = soup.find("span", "mb3 full-width").string.strip('\t\n ').lower()  # Name below Brand
                pic_desc = soup.find("div", "fs11 ml50 c999 wid-357 clear")  # ANy Information Under primary Image
                size_chart = soup.find("a", "c666 fl txt-deco-under fs11")  # sizechart
                if pic_desc:
                    pic_desc = pic_desc.string.strip('\t\n ').lower()
                d_data = soup.find("div", {"class": "thumb-slider pos-abs"})  # for total no of images
                pics = d_data.findAll("span")
                no_of_pics = len(pics)  # the number of pics in the web page.
                div_data = soup.find("div", {"class": "product-info c999 fs12 mb20"})  # specifications
                gender = soup.find("a", {"id": "qa-breadcrumb2"})  # gender from top
                clothing = soup.find("a", {"id": "qa-breadcrumb3"})
                watches = soup.find("a", {
                    "id": "qa-breadcrumb4"})  # category from top #category of the product after its type e.g.(Home | Men | Clothing | "Polos & Tees")
                sizes = soup.find("ul", {
                    "class": "prd-option-collection apw_size prd-size fs11 clrfix"})  # multiple sizes below mrp
                bric = "SELECT * FROM `Brick` WHERE `Name` = '" + brick + "'"
                db.execute(bric)
                tnumbrick = []
                for x in db:
                    tnumbrick.append(x)
                try:
                    if tnumbrick[1] < no_of_pics:  # checks the no. of pics with the compliance db.
                        ecode += ",Error in number of images"
                        print SKUU + "," + "Error in number of images" + "," + str(no_of_pics) + "," + str(
                            tnumbrick[0][1])
                except:
                    hi = "Hello"

                # ---------------------------- Checkpoint, start descripencies here ------------------------------------
                qq = ""
                if pic_desc and "size" in pic_desc:
                    qq = pic_desc.split("size")[1].strip(" ").strip(".")
                if clothing and gender and pic_desc:
                    clothing = clothing.string.strip('\t\n ').lower()
                    gender = gender.string.strip('\t\n ').lower()
                    if watches:
                        watches = watches.string.strip('\t\n ').lower()
                    if clothing in "clothing":
                        if gender.strip() == "men" and brick.lower().strip() not in v_others.no_vitals:
                            if "height" not in pic_desc or "chest" not in pic_desc or "waist" not in pic_desc:
                                ecode += ",Incomplete Vitals"
                                print SKUU + "," + "Incomplete Vitals" + "," + "Men" + ",\"" + pic_desc + "\""
                        if gender == "women" and brick.lower().strip() not in v_others.no_vitals:
                            if "height" not in pic_desc or "bust" not in pic_desc or "waist" not in pic_desc or "hip" not in pic_desc:
                                ecode += ",Incomplete Vitals"
                                print SKUU + "," + "Incomplete Vitals" + "," + "Women" + ",\"" + pic_desc + "\""
                for a in div_data.findAll("p"):
                    description = a.text.strip(' ')
                # where is the exception handler for catching the pic_desc which is out of the assigned div??
                row = soup.find("table", {"class": "c999 fs12 mt10 f-bold"}).findAll('tr')

                ss = {}
                # model Vital
                if pic_desc:
                    if "height" in pic_desc:
                        index = pic_desc.index("height") + 7
                        val = pic_desc[index] + pic_desc[index + 1] + pic_desc[index + 2] + pic_desc[index + 3]
                        if val not in v_others.height_range:
                            ecode += ",Invalid Height"
                            print SKUU + "," + "Invalid Height" + "," + str(v_others.height_range[0]) + "-" + str(
                                v_others.height_range[-1]) + "," + str(val)
                    if "chest" in pic_desc:
                        index = pic_desc.index("chest") + 6
                        val = pic_desc[index] + pic_desc[index + 1]
                        if not unicode(val).isnumeric():
                            ecode += ",Invalid Chest Size"
                            print SKUU + "," + "Invalid Chest Size" + "," + " " + "," + str(val)
                    if "waist" in pic_desc:
                        index = pic_desc.index("waist") + 6
                        val = pic_desc[index] + pic_desc[index + 1]
                        if not unicode(val).isnumeric():
                            ecode += ",Invalid Waist Size"
                            print SKUU + "," + "Invalid Waist Size" + "," + " " + "," + str(val)
                    if "bust" in pic_desc:
                        index = pic_desc.index("bust") + 5
                        val = pic_desc[index] + pic_desc[index + 1]
                        if not unicode(val).isnumeric():
                            ecode += ",Invalid Bust Size"
                            print SKUU + "," + "Invalid Bust Size" + "," + " " + "," + str(val)
                    if "hip" in pic_desc:
                        if "hips" in pic_desc:
                            ecode += ",Hips mentioned in vitals"
                            index = pic_desc.index("hips") + 5
                        else:
                            index = pic_desc.index("hip") + 4
                        val = pic_desc[index] + pic_desc[index + 1]
                        if not unicode(val).isnumeric():
                            ecode += ",Invalid Hip Size"
                            print SKUU + "," + "Invalid Hip Size" + "," + " " + "," + str(val)
                if sizes and qq is not "":
                    size = sizes.findAll("li")
                    twem = len(size)
                    if not size_chart and twem > 1:
                        ecode += ",Chart Absent"
                        print SKUU + "," + "Chart Absent" + "," + " " + "," + str(twem)
                    a = ['free size', 'standard', 'regular']  # freesize ,standard, regular array
                    for x in a:
                        if x in pic_desc:
                            ecode += ",Free/Standatd/Regular mentioned as size"
                            print SKUU + "," + "Free/Standatd/Regular mentioned as size" + ",\"" + pic_desc + "\"," + x
                    for i in range(0, twem):
                        ss[i] = size[i].string.strip('\t\n ').lower()
                    if ss[0] in a and "size" in pic_desc:
                        ecode += ",Model vitals has size with Free Size"
                    if ss[0] in a and size_chart:
                        ecode += ",Size Chart present with Free Size/Standard/Regular"
                    if qq not in ss.values() and qq not in "free":
                        ecode += ",Size worn by model not present in select size options"
                bag_list = ["sling bag", "backpack", "duffel bags", "bags", "laptop bag", "laptop backpack",
                            "messenger bags", "shopping bag", "school bag", "travelling bag", "sports bag",
                            "laptop briefcase", "multiutility bag"]

                # --------- Stats ----------
                temp = len(row)
                description = " " + description
                c = count
                u = url
                n = name
                bn = brand_name
                nbb = name_below_brand
                de = description.lower()
                if not description:
                    ecode += ",Description Not Present"
                if description not in " ":
                    sp_de = de.strip().encode('utf-8').split(".")
                else:
                    sp_de = "Hi"
                if sp_de[-1] is "":
                    del sp_de[-1]
                # to catch the exception of pairing of clothes.
                if ("team" in sp_de[-1] or "pair" in sp_de[-1] or "wear" in sp_de[-1] or "club" in sp_de[
                    -1] or "style" in sp_de[-1]) and "with" in sp_de[-1]:
                    del sp_de[-1]
                de = ".".join(sp_de)
                cnt = 0
                scolo = {}
                for w in v_color.all:
                    if w in de:
                        if not scolo:
                            scolo[cnt] = w.strip()
                            cnt += 1
                        else:
                            for mk in range(len(scolo)):
                                if scolo[mk]:
                                    if w.strip() not in scolo[mk]:
                                        scolo[cnt] = w.strip()
                                        cnt += 1
                # Array's for neck, sleeves , length , Closing_list , linning_list
                nid = []
                if "neck" in de:
                    for m in v_adv.neck:
                        if m in de:
                            nid.append(m.replace("neck", "").strip())
                sid = []
                if "sleeve" in de:
                    for m in v_adv.sleeves:
                        if m in de:
                            sid.append(m)
                lid = []
                for m in v_adv.length:
                    if m in de:
                        lid.append(m)
                cid = []
                for m in v_adv.closing:
                    if m in de:
                        cid.append(m)
                liid = []
                for m in v_adv.lining:
                    if m in de:
                        liid.append(m)
                hid = []
                for m in v_adv.heelshape:
                    if m in de:
                        hid.append(m)
                soid = []
                for m in var.v_adv.sole_material:
                    if m in de:
                        soid.append(m)
                umid = []
                for m in var.v_adv.upper_material:
                    if m in de:
                        umid.append(m)
                styleid = []
                for m in v_adv.style:
                    if m in de:
                        styleid.append(m)
                fid = []
                if "fit" in de:
                    for m in v_adv.fit:
                        if m in de:
                            fid.append(m.replace("fit", "").replace("-", "").strip())
                if not scolo:
                    scolo = None
                brand_name = brand_name.split()
                lol = u"[\'](.),;:-!?&"  # regex to remove any kind of useless characters from the description of the product.
                # description check
                description = description.replace(unichr(160), " ")
                trantab = maketrans(lol, "             ")
                description = description.encode('utf-8').translate(trantab)

                description = description.split()
                # Removing stop words

                # remove_stopword(description)
                """spellcheck = 0
                erword = []
                for word in description:
                    if not d.check(word):
                        erword.append(word)
                        spellcheck = 1
                if spellcheck == 1:
                    ecode += ",Spelling mistake in description"
                    print SKUU + "," + "Spelling mistake in description" + ",\"" + de + "\",\"" + ",".join(erword) + "\""""

                details = {}
                # print row
                # erword = ",".join(erword)
                # "DATA IN TABLE"
                # color check

                for i in range(0, temp - 1):

                    cells = row[i].findAll("td", limit=2)
                    if cells[1].get_text():
                        if cells[0].get_text():
                            details[cells[0].get_text().strip('\t\n ').lower()] = cells[1].get_text().lower()
                color_in_name = []
                dk = details.keys()
                if watches and not isinstance(watches, unicode):
                    watches = watches.string.strip('\t\n ').lower()
                color = ""
                material = ""
                # print details
                e_color = None
                for w in v_color.all:
                    if w.strip() in name:
                        color_in_name.append(w.strip())
                if watches:
                    if watches in "watches":
                        try:
                            value = details['strap color']
                            if value:
                                color = details['strap color']

                        except KeyError:
                            hi = "hellop"
                    elif watches in "sunglasses":
                        if 'lens color' in details.keys():
                            color = details['lens color']
                            if 'frame color' in details.keys():
                                if details['frame color'].strip() not in color_in_name:
                                    if details['frame color'].strip().replace(" ", "-") not in color_in_name:
                                        if len(color_in_name) > 1:
                                            ecode += ",Frame Color mismatch in name"
                                            print SKUU + "," + "Frame Color mismatch in name" + "," + details[
                                                'frame color'] + ",\"" + ",".join(color_in_name) + "\""
                                        else:
                                            ecode += ",Frame Color missing"
                            else:
                                ecode += ",Frame Color missing in attributes"
                            if details['lens color'].strip() not in color_in_name:
                                if details['lens color'].strip().replace(" ", "-") not in color_in_name:
                                    if len(color_in_name) > 1:
                                        ecode += ",Lens Color mismatch in name"
                                        print SKUU + "," + "Lens Color mismatch in name" + "," + details[
                                            'lens color'] + ",\"" + ",".join(color_in_name) + "\""
                        else:
                            ecode += ",No Color"
                            color = "No Color"
                    elif 'color' in details.keys():
                        color = details['color']

                    else:
                        ecode += ",No Color"
                        color = "No Color"

                color = color.strip().replace(" ", "-")
                if color in ["na","n/a"]:
                    ecode += ",Color N/A error"
                if 'material' in details.keys():
                    material = details['material']
                if 'neck' in details.keys():
                    if details['neck'].replace("neck", "").strip() not in nid and len(nid) >= 1:
                        ecode += ",Neck details mismatch in description"
                        print SKUU + "," + "Neck details mismatch in description" + "," + details[
                            'neck'] + ",\"" + ",".join(nid) + "\""
                if 'sleeves' in details.keys():
                    if details['sleeves'] not in sid and len(sid) >= 1:
                        ecode += ",Sleeves details mismatch in description"
                        print SKUU + "," + "Sleeves details mismatch in description" + "," + details[
                            'sleeves'] + ",\"" + ",".join(sid) + "\""
                if 'length' in details.keys():
                    if details['length'] not in lid and len(lid) >= 1:
                        ecode += ",Length details mismatch in description"
                        print SKUU + "," + "Length details mismatch in description" + "," + details[
                            'length'] + ",\"" + ",".join(lid) + "\""
                if 'toe shape' in details.keys():
                    if details['toe shape'] not in de:
                        ecode += ",Toe Shape details mismatch in description"
                if 'closing' in details.keys():
                    if details['closing'] not in cid and len(cid) >= 1:
                        ecode += ",Closing details mismatch in description"
                        print SKUU + "," + "Closing details mismatch in description" + "," + details[
                            'closing'] + ",\"" + ",".join(cid) + "\""
                if 'lining' in details.keys():
                    if details['lining'] not in liid and len(liid) >= 1:
                        ecode += ",Lining details mismatch in description"
                        print SKUU + "," + "Lining details mismatch in description" + "," + details[
                            'lining'] + ",\"" + ",".join(liid) + "\""
                if 'heel shape' in details.keys():
                    if details['heel shape'] not in hid and len(hid) >= 1:
                        ecode += ",Heel Shape details mismatch in description"
                        print SKUU + "," + "Heel Shape details mismatch in description" + "," + details[
                            'heel shape'] + ",\"" + ",".join(hid) + "\""
                if 'sole material' in details.keys():
                    if details['sole material'] not in soid and len(soid) >= 1:
                        ecode += ",Sole Material details mismatch in description"
                        print SKUU + "," + "Sole Material details mismatch in description" + "," + details[
                            'sole material'] + ",\"" + ",".join(soid) + "\""
                if 'upper material' in details.keys():
                    if details['upper material'] not in umid and len(umid) >= 1:
                        ecode += ",Upper Material details mismatch in description"
                        print SKUU + "," + "Upper Material details mismatch in description" + "," + details[
                            'upper material'] + ",\"" + ",".join(umid) + "\""
                if 'style' in details.keys():
                    if details['style'] not in styleid and len(styleid) >= 1:
                        ecode += ",Style details mismatch in description"
                        print SKUU + "," + "Style details mismatch in description" + "," + details[
                            'style'] + ",\"" + ",".join(styleid) + "\""
                if 'fit' in details.keys():
                    if details['fit'].replace("fit", "").replace("-", "").strip() not in fid and len(fid) >= 1:
                        ecode += ",Fit details mismatch in description"
                        print SKUU + "," + "Fit details mismatch in description" + "," + details[
                            'fit'] + ",\"" + ",".join(fid) + "\""
                if 'occasion' in details.keys():
                    if details['occasion'] not in de:
                        ecode += ",Occasion details mismatch in description"
                cont = 0
                # material check

                if category in "ACC":
                    material_details = v_others.acc
                elif category in "JEWELLRY":
                    material_details = v_others.jewellery
                elif category in "APPAREL":
                    material_details = v_others.apparels
                elif category in "HOME":
                    material_details = v_others.home
                elif category in "FOOTWEAR":
                    material_details = v_others.footwear_mat
                elif category in "BEAUTY":
                    material_details = v_others.beauty
                elif category in "FRAGRANCES":
                    material_details = v_others.beauty
                elif category in "TOYS":
                    material_details = v_others.toys
                elif category in "ACTSPRTS":
                    material_details = v_others.actsprts
                else:
                    material_details = v_others.apparels
                if category in "APPAREL" or "apparel":
                    if not pic_desc:
                        ecode += ",Model Vitals Absent"

                if brick.lower() in bag_list:
                    if not pic_desc:
                        ecode += ",Model Vitals Absent"
                if brick.lower() in bag_list and pic_desc:
                    if "height" not in pic_desc:
                        ecode += ",Incomplete mannequin vitals"

                if material:
                    mat = {}
                    m = map(str, regex.findall(r'\d+', material)) + map(str, regex.findall(r'%', material))
                    for re in material_details:
                        if re in de:
                            for kl in m:
                                re = re.replace(kl, "").strip()
                            if cont is 0:
                                mat[cont] = re.strip()
                                cont += 1
                            else:
                                for mk in range(len(mat)):
                                    if mat[mk]:
                                        if re not in mat[mk]:
                                            mat[cont] = re.strip()
                                            cont += 1
                    if len(mat) > 0:
                        temp_mat = material
                        for x in m:
                            temp_mat = temp_mat.replace(x, "").strip()
                        if temp_mat not in mat.values():
                            ecode += ",Mismatch in material"
                            print SKUU + "," + "Mismatch in material" + ",\"" + material + "\",\"" + ",".join(
                                mat.values()) + "\""
                            # material check ends
                            # name below brand error
                if name == name_below_brand:

                    e_brand = None
                else:
                    e_brand = "Error in name_below_brand"

                if 'assorted' in name_below_brand:
                    if 'multi' in color:
                        ecode += ",Multi is mentioned in color"
                    elif 'assorted' in color:
                        ecode += ""
                if 'multi' in name_below_brand:
                    if 'assorted' in color:
                        ecode += ",Assorted is mentioned in color"
                    elif 'multi' in color:
                        ecode += ""
                        # color
                if color in v_color.all:
                    mayu = 0
                    for color_name in v_color.all:
                        if color_name.strip() in name:
                            mayu = 1
                        else:
                            wastewwww1 = 0
                    if mayu == 1:
                        if color.strip() in name:
                            hi = "hi"
                        else:
                            ecode += ",There is color mismatch in Name"
                    else:
                        ecode += ",No color in Name"

                else:
                    ecode += ",Color not found in colors list"
                if color.strip() in "multi":
                    scolo = {0: "multi"}
                colordiff = []
                color1 = []
                if scolo:                           # ------------------------- Checkpoint -----------------------------
                    p = []
                    p = scolo.values()
                    p = [x.strip().replace(" ", "-") for x in p]  # to match the color descriptions accurately
                    tempcolor = "-".join(color.strip().split(" "))
                    if tempcolor in v_color.grey and list(set(p) & set(v_color.grey)):
                        flag = 0
                        for x in list(set(p) & set(v_color.grey)):
                            if x in v_color.grey[-1]:
                                flag = 1
                        if tempcolor in v_color.grey[-1] or flag or tempcolor in p:
                            pass
                        else:
                            ecode += ",Color mismatch in description"
                            print SKUU + "," + "Color mismatch in description" + ",\"" + ",".join(
                                scolo.values()) + "\"," + color
                    elif tempcolor in v_color.blue and list(set(p) & set(v_color.blue)):
                        flag = 0
                        for x in list(set(p) & set(v_color.blue)):  # done to improve the search speed.
                            if x in v_color.blue[-1]:
                                flag = 1
                        if tempcolor in v_color.blue[-1] or flag or tempcolor in p:
                            pass
                        else:
                            ecode += ",Color mismatch in description"
                            print SKUU + "," + "Color mismatch in description" + ",\"" + ",".join(
                                scolo.values()) + "\"," + color
                    elif tempcolor in v_color.silver and list(set(p) & set(v_color.silver)):
                        flag = 0
                        for x in list(set(p) & set(v_color.silver)):
                            if x in v_color.silver[-1]:
                                flag = 1
                        if tempcolor in v_color.silver[-1] or flag or tempcolor in p:
                            pass
                        else:
                            ecode += ",Color mismatch in description"
                            print SKUU + "," + "Color mismatch in description" + ",\"" + ",".join(
                                scolo.values()) + "\"," + color
                    elif tempcolor in v_color.red and list(set(p) & set(v_color.red)):
                        flag = 0
                        for x in list(set(p) & set(v_color.red)):
                            if x in v_color.red[-1]:
                                flag = 1
                        if tempcolor in v_color.red[-1] or flag or tempcolor in p:
                            pass
                        else:
                            ecode += ",Color mismatch in description"
                            print SKUU + "," + "Color mismatch in description" + ",\"" + ",".join(
                                scolo.values()) + "\"," + color
                    elif tempcolor in v_color.milange and list(set(p) & set(v_color.milange)):
                        flag = 0
                        for x in list(set(p) & set(v_color.milange)):
                            if x in v_color.milange[-1]:
                                flag = 1
                        if tempcolor in v_color.milange[-1] or flag or tempcolor in p:
                            pass
                        else:
                            ecode += ",Color mismatch in description"
                            print SKUU + "," + "Color mismatch in description" + ",\"" + ",".join(
                                scolo.values()) + "\"," + color
                    elif tempcolor in v_color.white and list(set(p) & set(v_color.white)):
                        flag = 0
                        for x in list(set(p) & set(v_color.white)):
                            if x in v_color.white[-1]:
                                flag = 1
                        if tempcolor in v_color.white[-1] or flag or tempcolor in p:
                            pass
                        else:
                            ecode += ",Color mismatch in description"
                            print SKUU + "," + "Color mismatch in description" + ",\"" + ",".join(
                                scolo.values()) + "\"," + color
                    else:
                        if color.strip() not in scolo.values():
                            if color.strip().replace(" ", "-") not in scolo.values():
                                ecode += ",Color mismatch in description"
                                print SKUU + "," + "Color mismatch in description" + ",\"" + ",".join(
                                    scolo.values()) + "\"," + color

                                # Package Contents
                ar = ['set of', 'pack of', 'combo of']
                ar1 = ['suit set']
                for mm in ar:
                    col = None
                    if mm.lower() in de:
                        k = len(mm)
                        d = de.index(mm) + k
                        col = de[d + 1]
                    if col:
                        if col.isdigit():
                            if 'package contents' in details.keys():
                                if col not in details['package contents']:
                                    ecode += ",Error in Package Contents"
                            else:
                                ecode += ",Package contents absent"

                for me in ar1:
                    if me in de:
                        if 'package contents' in details.keys():
                            bb = 1
                        else:
                            ecode += ",Package contents absent"
                if ecode:  # image
                    if brick.lower() in v_others.shadecard_bricks:
                        anacolo = str(read_image(no_of_pics, prod_id, brick))
                    else:
                        anacolo = str(read_image(no_of_pics, prod_id))
                    if anacolo in "":
                        ecode += ",Unable to load Image"
                    else:
                        singlecolo = anacolo.strip().split(",")
                        # print singlecolo
                        coloarray = []  # UNCOMMENT THIS WHEN COLOR NAMES ARE READY
                        for i in range(len(singlecolo)):
                            if singlecolo[i] is not "":
                                coloarray.append(colorname(singlecolo[i]))
                        if color.strip() not in coloarray:
                            if find_parent(color.strip()) not in coloarray:
                                ecode += ",Error in Color in Image"
                                print SKUU + "," + "Error in Color in Image" + ",\"" + ",".join(
                                    coloarray) + "\"," + color

                    qam = "INSERT IGNORE INTO sku VALUES ('" + details[
                        'sku'].strip() + "','" + category + "','" + brick + "','" + dba.escape(
                        u) + " ','" + prod_id + "','" + anacolo + "','" + dba.escape(
                        Brandd) + "','" + MRP + "','" + ItemType + "')"
                    #	print qam
                    # qam = "INSERT IGNORE INTO sku VALUES ('" + details['sku'].strip() + "','" + category + "','" + brick + "','" + u +" ','" + prod_id + "','"+ anacolo +"','" + Brandd +"','"+MRP+"')"
                    # print "anacolo : " + anacolo
                    # db.execute(qam)
                    # dba.commit()
                    # Spell Check
                    ecode = ecode.split(",")
                    for letter in ecode:
                        if letter is not "":

                            if letter in codes.keys():
                                if letter in "Spelling mistake in description":
                                    spel = unicode(erword, errors='ignore')
                                else:
                                    spel = ""
                                skuerr = "INSERT IGNORE INTO discri (`SKU`,`error`,`Speller`) VALUES('" + str(
                                    details['sku'].strip()) + "','" + str(codes[letter]) + "','" + spel + "')"
                                db.execute(skuerr)
                                dba.commit()
        db.close()
        dba.close()
        del db
        del dba
        sys.exc_clear()
        sys.exc_traceback = sys.last_traceback = None

    except:
        # raise
        print "skipped link number:", count
        file = open('skipped_links.csv', 'a+')
        file.write(url + ",\n")
        file.close()
        db.close()
        dba.close()
        del db
        del dba
        sys.exc_clear()
        sys.exc_traceback = sys.last_traceback = None

# --------------------------------------------------- Checkpoint 3 -----------------------------------------------------

farm = open("xaa", "r")
farmdata = csv.reader(farm)
ddddd = []
for x in farmdata:
    ddddd.append(x)
farm.close()
while (1):
    # db=_mysql.connect(host="localhost",user="root",passwd="jabong@123",db="discrepancy")

    try:
        if count == 1 and sys.argv[2].strip() is "1":
            dba = pymysql.connect(host="localhost", user="root", passwd="", db="discrepancy")  # discrpancy
            db = dba.cursor()
            selq = "INSERT IGNORE INTO runat (`Start_time`,`code`) VALUES ('" + time.strftime(
                "%Y-%m-%d") + " " + time.strftime("%X") + "','" + sys.argv[1] + "')"
            db.execute(selq)
            dba.commit()
            del db
            del dba
        url = ddddd.pop()
        get_articles(url[10].strip("\"\n\r"), url[9].strip("\"\n\r"), url[4].strip("\"\n\r"), url[2].strip("\"\n\r"),
                     url[0].strip("\"\n\r"), url[1].strip("\"\n\r"), url[8].strip("\"\n\r"), url[11].strip("\"\n\r"))

        # get_articles(url[10].strip("\"\n\r"),url[9].strip("\"\n\r"),url[4].strip("\"\n\r"),url[2].strip("\"\n\r"),url[0].strip("\"\n\r"),url[1].strip("\"\n\r"),url[8].strip("\"\n\r"))
        count = count + 1
        sys.exc_clear()
        sys.exc_traceback = sys.last_traceback = None
    except IndexError:
        print "correct the csv and retry"
    # raise
    except EOFError:
        dba = pymysql.connect(host="localhost", user="root", passwd="", db="discrepancy")  # discrpancy
        db = dba.cursor()
        selq = "UPDATE runat SET `end_time`= '" + time.strftime("%Y-%m-%d") + " " + time.strftime(
            "%X") + "' WHERE code = '" + sys.argv[1] + "'"
        db.execute(selq)
        dba.commit()
        html = requests.get("http://202.191.153.65/ankit/discre.php?rr=" + sys.argv[2])
        quit()
