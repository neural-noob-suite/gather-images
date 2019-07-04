#!/usr/bin/env python3

# https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py

import sys
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import tensorflow as tf


flags = tf.app.flags
flags.DEFINE_string('output_path', '', 'Path to output csv file')
flags.DEFINE_string('image_dir', '', 'Path to images')
FLAGS = flags.FLAGS

if FLAGS.output_path == '':
    print('output_path missing')
    sys.exit(1)

if FLAGS.image_dir == '':
    print('image_dir missing')
    sys.exit(1)


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = os.path.join(os.getcwd(), FLAGS.image_dir)
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv(FLAGS.output_path, index=None)
    print('Successfully converted xml to csv.')


main()
