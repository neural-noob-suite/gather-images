#!/usr/bin/env python
# encoding: utf-8
"""
Usage:
  # Script to resize all files in current directory,
    saving new .jpg images in a new folder. 
  # eg. python resize.py 
"""

import cv2
import glob
import os
import sys
import argparse

max_size = 512
input_folder = None
output_folder = 'resized'

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--max_size", type=int, default=max_size,
                    help="the maximal image width/height")
parser.add_argument("-i", "--input", help="input folder for images")
parser.add_argument("-d", "--dest", default=output_folder,
                    help="destitation folder for resized images")
args = parser.parse_args()

max_size, input_folder, output_folder = args.max_size, args.input, args.dest

if input_folder is None:
    print('input folder missing')
    sys.exit(1)


def resize():
    # find all jpg images
    imgs = glob.glob(input_folder + '/*.jpg')
    print('Found files %s' % len(imgs))
    print('Resizing all images be %d pixels wide or height' % max_size)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through resizing and saving
    for img in imgs:
        pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        ht, wd = pic.shape[0], pic.shape[1]
        print(img, wd, ht)
        if wd >= ht:
            width = max_size
            height = int(width * ht / wd)
        else:
            height = max_size
            width = int(height * wd / ht)
        pic = cv2.resize(pic, (width, height))

        filename_w_ext = os.path.basename(img)
        output_path = output_folder + '/' + filename_w_ext
        cv2.imwrite(output_path, pic)


if __name__ == "__main__":
    resize()
