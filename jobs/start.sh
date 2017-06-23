#!/bin/bash
#####
# Sarts the camera module and the web backend
#####
echo "sarting Python camera module..."
nohup sudo python camera_main.py &

echo "starting node backend"
nohup sudo npm start &
