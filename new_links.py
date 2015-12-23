from bs4 import BeautifulSoup
import time
import sys
import requests
from string import maketrans
import csv

import pymysql
from image import read_image  # imgtest=>image
from colors import colorname
from variables import height_range, color_list, shadecard_bricks, beauty, toys, home, jewellery, acc, apparels
from variables import no_vitals, upper_material, footwear_mat, sole_material, grey, silver, red, milange, white, \
    antique, blue, yellow
from variables import neck_list, sleeves_list, closing_list, linning_list, fit_list, style_list, heelshape_list, \
    length_list
import re as regex

if len(sys.argv) < 3:
    print "Please enter a runcode and console code"
    quit()
