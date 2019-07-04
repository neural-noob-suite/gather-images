# gather-images

This repo contains scripts to help gathering/labeling images for ML. Read
the scripts to learn more about them

```
pip install -r requirements.txt
./gather.sh
./remove_non_images.py
OUTPUT_DIR=all_images ./filter.sh
./delete_duplicates.sh all_images/*
./resize.py --input=all_images -m 500
./label.sh
./split.py --percent=20 --input=all_images
./xml_to_csv.py --output_path=train_labels.csv --image_dir=all_images
./generate_tfrecord.py --csv_input=train_labels.csv --output_path=tf.record --image_dir=all_images
```

## gather.sh

Gather will do google image searches and save the images. The keywords searched
can be found in `keywords.txt`. Images will be downloaded in a `downloads`
folder

## remove_non_images.py

Removes files which were downloaded and are not jpeg/png images

## filter.sh

Filter will show a baisc GUI to the user asking if this image should be used
in labeling or not.

If user selects yes, the file will be copied to OUTPUT_DIR

## delete_duplicates.sh

Removes duplicated images based on md5 hash

## resize.py

Resize all images to a specific max width/height

## label.sh

The script will run [labelImg](https://github.com/tzutalin/labelImg). Make sure
you select the correct save directory. It should be the same as the
`OUTPUT_DIR` folder so files and their labels will be in the same place.

labelImg keyboard shortcuts:

  * w add label
  * a prev image in folder
  * d next image in folder

## split.py

Split the images in 2 folders, one folder will contain the specified percent
of images.

## xml_to_csv.py

Reads all xml files and stores the data which is needed as a csv file

## generate_tfrecord.py

Creates the TFRecord
