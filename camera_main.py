#!/usr/bin/python

#from picamera import PiCamera
from SimpleCV import *
from datetime import datetime

import logging
import os
import time

def main():
    print ("starting... ")
    
    logging.basicConfig(level=logging.DEBUG, filename="/tmp/camera_main.log")

    #cam = Camera(prop_set={'width': 1024, 'height': 768})
    maxMean = 0
    cam = Camera()

    #display = Display((1024, 768))

    while True:
        tstart = time.time()
        
        doCapture(cam, maxMean)
        
        tfinish = time.time()
        print ("time ellapsed: {0}".format(tfinish - tstart))


def doCapture(cam, maxMean):
    # grabs original image to be used when motion is detected
    original = cam.getImage()
    timestamp = datetime.now().strftime("%a, %b, %-d %Y %H:%M:%S")
    original.drawText(timestamp, 10, 10, color=Color.ORANGE, fontsize=20)
    
    # takes two shots in sequence (we will compare them to detect motion)        
    img01 = cam.getImage().toGray()
    time.sleep(0.5)
    img02 = cam.getImage().toGray()

    # 
    diff = (img01 - img02).binarize(50).invert()
    #diff.show()

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

main()

##img1 = cam.getImage().invert()
##img1.save('image_invert.png')
##
##img1 = cam.getImage().binarize(90)
##img1.save('image_binarize.png')
##
##img1 = cam.getImage().edges()
##img1.save('image_edges.png')








