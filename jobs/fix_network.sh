#!/bin/bash
#####
# checks network status and restart it if down
#
# Add the following to your crontab to run every 5 minuets
# sudo nano /etc/crontab
#   */5 *    * * *    root    /usr/bin/network_checker.sh
#    #Source : http://root42.blogspot.com/2013/03/how-to-make-raspberry-pi-automatically.html
#####
# 8.8.8.8 is the Google Public DNS IP
TESTIP=8.8.8.8
ping -c2 ${TESTIP} > /dev/null
if [ $? != 0 ]
then
   echo "network seems to be down. Will restart - at ${date}"

   ifdown --force wlan0
   ifup wlan0
#   /etc/init.d/networking restart
#   omxplayer -o local --vol -1750 /opt/sonic-pi/etc/samples/ambi_choir.wav
   service ssh restart
#   service xrdp restart
fi