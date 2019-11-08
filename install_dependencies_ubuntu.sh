#!/bin/bash

#install python  Dependencies
sudo apt update
sudo apt install python3-pip
pip3 install psutil
pip3 install bottle
pip3 install configparser

#Install and configure Telegraf
# download the package to the VM 
wget https://dl.influxdata.com/telegraf/releases/telegraf_1.8.0~rc1-1_amd64.deb 
# install the package 
sudo dpkg -i telegraf_1.8.0~rc1-1_amd64.deb