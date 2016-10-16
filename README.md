# camera_project

## Goal
This is a simple camera monitoring system which aims to accomplish the following tasls:

* Continuously takes pictures and compares them in order to detect motion
* Once motion is detected, saves the pictures that have beem compared
* Creates a timelipse video once a day including the periods of time when motion has been detected
* Emails the timelapse video to a specified recipient(s)

The system also provides an HTML interface where users can see the current camera capture for real-time view.

## Setup
In order to start up the camera monitoring system, we need to start two different processes:

1. Open a SSH session on Raspberry Pi 
2. start the camera_main.py process:
    * nohup sudo python camera_main.py &
3. start node.js front-end site:
    * nohup sudo npm start &

You can safely close the SSH remote session as the processes will continue running on your Pi.