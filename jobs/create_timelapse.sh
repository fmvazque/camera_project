#!/bin/bash
echo "starting..."

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

SRCDIR="/home/pi/western/public/picamera/$YEAR/$MONTH/$DAY"
TMPDIR="${SRCDIR}/temp"

cd ${SRCDIR}

# copy files to a temporary folder for processing
if [ ! -d ${TMPDIR} ]; then
	mkdir -p ${TMPDIR}
fi

# list the files sorted by name (ls default) and outputs the list of files to a txt file
ls image_??????????.png | sort > ${TMPDIR}/files_to_process.txt 

# reads the txt file line by line and for each file listed there, copies it to the temp folder 
# to be subsequently used to create the timelapse video.
while read filename  ; do
    N=$((N+1))
    echo $filename
	str_n=$(`echo printf "%04d" $N`)
	echo $str_n
	cp -n $filename ${TMPDIR}/image_${str_n}.png
done < ${TMPDIR}/files_to_process.txt

# creates the timelapse video from the files in the temp directory
IMAGES_TEMPLATE=${TMPDIR}"/image_%04d.png"
avconv -y -r 20 -i ${IMAGES_TEMPLATE} -r 10 -vcodec libx264 -crf 20 -g 15 ${SRCDIR}/timelapse.mp4

# remove the temp folder and its contents
#rm -rf ${TMPDIR}

# send email 
echo "Here is today's timelapse of your 'muita treta, vixi' monitoring. Enjoy!" | mail -s "Picu&Bola Monitoring - Todays's timelapse (${MONTH}/${DAY}/${YEAR})" fabiovazquez@outlook.com --attach=${SRCDIR}/timelapse.mp4
echo "Here is today's timelapse of your 'muita treta, vixi' monitoring. Enjoy!" | mail -s "Picu&Bola Monitoring - Todays's timelapse (${MONTH}/${DAY}/${YEAR})" drimv@outlook.com --attach=${SRCDIR}/timelapse.mp4