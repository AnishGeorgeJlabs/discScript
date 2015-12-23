#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Color Detection module
"""

import urllib
import subprocess
from string import maketrans
from PIL import Image
import sys

import os

prodid = "566765"

url = "http://www.jabong.com/47-maple-Brown-Leather-Wallet-566765.html"
# http://static.jabong.com/p/-681516-5-catalog.jpg
def read_image(no_of_pics, prodid, brick=""):
    # no_of_pics = len(pics)	# This variable counts the number of images that are available if its less than equal
    # to 4 report error
    imageurl = "http://static.jabong.com/p/-"
    id = prodid[::-1]
    try:
        if no_of_pics > 5:
            temp = no_of_pics - 1
            temp = str(temp)
            imageurl = imageurl + id + "-" + temp + "-catalog.jpg"
        if no_of_pics is 5:
            imageurl = imageurl + id + "-5-catalog.jpg"
        if no_of_pics <= 4 and brick is "":
            temp = no_of_pics
            temp = str(temp)
            imageurl = imageurl + id + "-" + temp + "-catalog.jpg"
        if brick is not "":
            imageurl = imageurl + id + "-1-catalog.jpg"
        f = open('test' + prodid + '.jpg', 'wb')
        f.write(urllib.urlopen(imageurl).read())
        f.close()
        if brick is not "":
            box = (143, 12, 165, 34)
            imageFile = "test" + prodid + ".jpg"
            try:
                im1 = Image.open(imageFile)
            except:
                return "#000000"
            region = im1.crop(box)
            region.save("test" + prodid + ".jpg")
        try:
            p1 = subprocess.Popen(['colorific', "test" + prodid + ".jpg"], stdout=subprocess.PIPE)
        except:
            return "#000000"
        output, error = p1.communicate()
        output = str(output)
        output = output.replace("test" + prodid + ".jpg\t", "")
        output = output.strip('\t\n ')
        trantab = maketrans("\t", ",")
        output = output.translate(trantab)
        os.remove("test" + prodid + ".jpg")
        sys.exc_clear()
        sys.exc_traceback = sys.last_traceback = None
        return output


    except IOError:
        print"Unable to read image"
    sys.exc_clear()
    sys.exc_traceback = sys.last_traceback = None


if __name__ == "__main__":
    print read_image(3, "638408", "Lipstick")
