# camera_project
camera 

In order to start up the camera monitoring system, we need to start two different processes:

1. Open a SSH session on Raspberry Pi 
2. start the camera_main.py process:
     nohup sudo python camera_mail.py &
3. start node.js front-end site:
     nohup sudo npm start &

You can safely close the SSH remote session as the processes will continue running on your Pi.