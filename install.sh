#!/bin/bash

# install apt dependencies
sudo apt update
sudo apt install python3 python3-pip espeak alsa-utils -y

# install python dependencies
pip3 install pyttsx3
