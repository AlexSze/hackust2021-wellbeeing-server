#!/bin/bash

mkdir /home/pi/wellbeeing
cp ./server.py /home/pi/wellbeeing
cp ./servo.py /home/pi/wellbeeing
cp ./run.sh /home/pi/wellbeeing
cp ./ngrok.yml /home/pi/wellbeeing
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
mv ./ngrok /home/pi/wellbeeing
rm ngrok-stable-linux-arm.zip
sudo cp ./ngrok.service /etc/systemd/system
sudo cp ./wellbeeing.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable wellbeeing.service
sudo systemctl enable ngrok.service


