#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import simpleaudio as sa

reader = SimpleMFRC522()

def play_beep():
    wave_obj = sa.WaveObject.from_wave_file("../assets/audio/beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

try:
    while True:
        id, text = reader.read()
        print(id)
        print(text)
        play_beep()
finally:
    GPIO.cleanup()