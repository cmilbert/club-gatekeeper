#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import simpleaudio as sa
import pyttsx3
 
tts_engine = pyttsx3.init()
reader = SimpleMFRC522()

def play_beep():
    wave_obj = sa.WaveObject.from_wave_file("../assets/audio/beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def say_welcome(name: str):
    tts_engine.say(f"Welcome {name}!")
    tts_engine.runAndWait()

try:
    while True:
        print("Please scan badge")
        id, text = reader.read()
        print(id)
        print(text)
        play_beep()
        say_welcome(text)

finally:
    GPIO.cleanup()