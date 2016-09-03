#!/usr/bin/python

from picamera import PiCamera
from SimpleCV import *
from datetime import datetime

import logging
import os

logging.basicConfig(level=logging.DEBUG, filename="/tmp/camera_main.log")

maxMean = 0
#cam = Camera(prop_set={'width': 1024, 'height': 768})
cam = Camera()

display = Display((1024, 768))

try:
    while True:
        display.checkEvents()

        # grabs original image to be used when motion is detected
        original = cam.getImage()
        
        # takes two shots in sequence (we will compare them to detect motion)        
        img01 = cam.getImage().toGray()
        time.sleep(0.5)
        img02 = cam.getImage().toGray()

        # 
        diff = (img01 - img02).binarize(50).invert()
        diff.show()

        matrix = diff.getNumpy()

        mean = matrix.mean()
        print (mean)

        if (mean > maxMean):
           maxMean = mean

        # saves current picture, which can be used to be shown on the UI
        original.save('./pics/current/current.png')    

        # if image diff is above threshold, save a copy of the image for later analysis
        if mean >= 0.1:
            date_path = datetime.now().strftime("%Y/%m/%d")
            dir_name = "./pics/{0}".format(date_path)

            # create directory if if does not exist
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)            

            epoch = int((datetime.now() - datetime(1970,1,1)).total_seconds())
            filename = "image_{0}".format(epoch)
            
            # original.save('./pics/' + filename + ".png")
            file_full_name = "{0}/{1}.png".format(dir_name, filename)

            print("saving file [{0}]".format(file_full_name)) 
            original.save(file_full_name)

            # saves binarized images for analysis
            # diff.save('./pics/binarized/' + filename + "_diff_mean_{0}.png".format(mean))
            
            print ('images saved')
            print ('max mean so far: {0}'.format(maxMean))

except:
    logging.exception("exception raised!!!")

##img1 = cam.getImage().invert()
##img1.save('image_invert.png')
##
##img1 = cam.getImage().binarize(90)
##img1.save('image_binarize.png')
##
##img1 = cam.getImage().edges()
##img1.save('image_edges.png')








