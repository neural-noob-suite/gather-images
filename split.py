#!/usr/bin/env python

import argparse
import os
import sys
import glob

from random import shuffle

percent = 30
input_folder = None
output_folder = 'split'

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--percent", type=int, default=percent,
                    help="the percentage of images to move to a different folder")
parser.add_argument("-i", "--input", help="destitation folder for resized images")
args = parser.parse_args()

percent, input_folder = args.percent, args.input


if input_folder is None:
    print('input folder missing')
    sys.exit(1)

if not os.path.exists(input_folder):
    print('input folder does not exist')
    sys.exit(1)

images = glob.glob(input_folder + '/' + '*.jpg')

# make sure all images have labeling
for image in images:
    filename_w_ext = os.path.basename(image)
    base_array = os.path.splitext(filename_w_ext)
    if not os.path.exists(input_folder + '/' + base_array[0] + '.xml'):
        print("%s is missing labeling" % filename_w_ext)
        sys.exit(1)


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

percent_count = int(len(images)*(percent / 100))
shuffle(images)
percent_of_images = images[0:percent_count]


for image in percent_of_images:
    filename_w_ext = os.path.basename(image)
    base_array = os.path.splitext(filename_w_ext)

    os.rename(input_folder + '/' + filename_w_ext, output_folder + '/' + filename_w_ext)
    os.rename(input_folder + '/' + base_array[0] + '.xml', output_folder + '/' + base_array[0] + '.xml')

print('Moved %s images' % len(percent_of_images))
