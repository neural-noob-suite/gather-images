#!/usr/bin/env python

import os

from PIL import Image
import imghdr

def check_path(path):
    try:
        with Image.open(path) as im:
            imgwhat = imghdr.what(path)
            if imgwhat is None:
                return False
            if imgwhat not in ['jpeg', 'jpg', 'png']:
                return False
        return True
    except IOError:
        return False

download_dir = r"downloads"
sub_dirs = [x[0] for x in os.walk(download_dir)]

for sub_dir in sub_dirs:
    for filename in os.listdir(sub_dir):
        path = sub_dir + "/" + filename
        if os.path.isfile(path):
            valid_img = check_path(path)
            if not valid_img:
                os.remove(path)
