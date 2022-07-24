#!/bin/bash

# Enable SPI if it is not enabled
echo "Enabling SPI interface for RFID reader"
sudo sed -i "s/#dtparam=spi=on/dtparam=spi=on/g" /boot/config.txt

# install apt dependencies
sudo apt update
sudo apt install python3 python3-pip espeak alsa-utils -y

# install python dependencies
pip3 install pyttsx3

echo "Rebooting"
sudo reboot 0