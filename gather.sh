#!/usr/bin/env sh

LIMIT=30

download_images() {
  googleimagesdownload \
    --keywords="$1" \
    --extract_metadata \
    --format="jpg" \
    --color_type="full-color" \
    --size=">2MP" \
    --type="photo" \
    --limit=$LIMIT
}

cat keywords.txt | while read line
do
  download_images "$line"
done
