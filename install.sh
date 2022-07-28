#!/bin/bash

# Enabling I2C if it is not enabled
echo "Enabling I2C interface for RFID reader"
sudo sed -i "s/#dtparam=i2c-arm=on/dtparam=i2c-arm=on/g" /boot/config.txt

# Enabling Serial
echo "Enabling Serial interface for RFID reader"
sudo sed -i "s/#enable_uart=1/enable_uart=1/g" /boot/config.txt

# install apt dependencies
sudo apt update
sudo apt install -y python3 python3-pip python3-dev python3-venv \
  espeak alsa-utils libopenjp2-7 python3-smbus i2c-tools

# install python dependencies
pip3 install pipx
source ~/.profile
pipx ensurepath
pipx install poetry

echo "Rebooting"
sudo reboot 0