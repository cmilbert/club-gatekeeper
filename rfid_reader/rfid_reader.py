#!/usr/bin/env python
from oled_091 import SSD1306
from subprocess import check_output
from time import sleep
from datetime import datetime
from os import path

import RPi.GPIO as GPIO
import simpleaudio as sa
import pyttsx3
import serial
 
class read_rfid:
    def read_rfid (self):
        ser = serial.Serial ("/dev/ttyS0")
        ser.baudrate = 9600
        data = ser.read(12)
        if(data != " "):
            GPIO.output(17,GPIO.HIGH)
            sleep(.2)
            GPIO.output(17,GPIO.LOW)
        ser.close ()
        data=data.decode("utf-8")
        return data

def welcome_print():
    display.PrintText("Scan Membership", FontSize=14)
    display.ShowImage()

def play_beep():
    wave_obj = sa.WaveObject.from_wave_file("../assets/audio/beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def say_welcome(name: str):
    tts_engine.say(f"Welcome {name}!")
    tts_engine.runAndWait()

tts_engine = pyttsx3.init()
display = SSD1306()
reader = read_rfid()

if __name__ == "__main__":
    try:
        while True:
            welcome_print()
            data = reader.read_rfid()
            print(data)
            play_beep()
            say_welcome(data)

    finally:
        GPIO.cleanup()