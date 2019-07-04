#!/usr/bin/env sh

# This scripts goes though each file in the downloads directory
# and asks the user a yes or no question. If the answer is yes,
# the file will be copied to the output folder to prepare for
# labeling

command -v yad >/dev/null 2>&1 || { echo >&2 "yad not installed. Run 'apt install yad'. Aborting."; exit 1; }

FILES=`find './downloads/' -type f | sort`

if [ -z "$OUTPUT_DIR" ]
then
  echo "OUTPUT_DIR enviornment variable missing"
  exit 1
fi
mkdir -p $OUTPUT_DIR

if [ -z "$1" ]
then
  INPUT=1
else
  INPUT=$1
fi

INPUT_NEXT=$((INPUT + 1))
CURRENT_FILE=`echo "$FILES" | sed -n "$INPUT"p`

echo $CURRENT_FILE

IMG_WIDTH=`identify "$CURRENT_FILE" | awk '{print $4}' | awk -F  "x" '{print $1}'`
IMG_HEIGHT=`identify "$CURRENT_FILE" | awk '{print $4}' | awk -F  "x" '{print $2}'`
if [ $IMG_WIDTH -gt 1600 ] || [ $IMG_HEIGHT -gt 1080 ]
then
  convert -resize 40% "$CURRENT_FILE" tmp.jpg
  DISPLAY_FILE="tmp.jpg"
else
  DISPLAY_FILE=$CURRENT_FILE
fi

echo $DISPLAY_FILE

yad \
  --buttons-layout=center \
  --question \
  --image="$DISPLAY_FILE" \
  --size=fit \
  --title="Use this image?" \
  --button=gtk-yes:0 \
  --button=gtk-no:1

case $? in
  0)
    FILENAME=$(basename -- "$CURRENT_FILE")
    INDEX=`printf "%06d\n" $INPUT`
    OUTPUT=$OUTPUT_DIR/$INDEX\_$FILENAME

    cp "$CURRENT_FILE" "$OUTPUT"
  ;;
  1)
    # do nothing
  ;;
  *)
    echo `ls -1 categorized | wc -l` files moved
    exit 0
  ;;
esac

# call the next input with the filter scripts
sh $(basename $0) $INPUT_NEXT
