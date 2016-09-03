#!/bin/bash

if [ $# -eq 0 ] 
then
	YEAR=$(date +%Y)
	MONTH=$(date +%m)
	DAY=$(date +%d)
else
	YEAR=$1
	MONTH=$2
	DAY=$3
fi

BASEDIR="/home/pi/camera_project"
SRCDIR="$BASEDIR/pics/$YEAR/$MONTH/$DAY"
BKDIR="/home/pi/western/public/picamera/$YEAR/$MONTH/$DAY"

echo $DAY
echo $MONTH
echo $YEAR

if [ ! -d "$BKDIR" ]; then
	mkdir -p $BKDIR
fi

# copy today's files to network share
IMAGE_TEMPLATE=${SRCDIR}"/image_*.png"
echo "copying files for ${IMAGE_TEMPLATE}..."
cp ${IMAGE_TEMPLATE} ${BKDIR}

# if copy command succeeded, we remove the files from the source location
if [ $? -eq 0 ]; then
	echo "deleting files from source location..."
    rm ${IMAGE_TEMPLATE}
else
    echo "file copy operation failed"
fi
