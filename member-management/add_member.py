import sqlite3
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import os

reader = SimpleMFRC522()
scanned = False
try:
    while scanned is False:
        print("Scan member card.")
        rfid, name = reader.read()
        scanned = True
finally:
    GPIO.cleanup()
con = sqlite3.connect(os.path.dirname(sys.argv[0]) + "/../members.db")
cur = con.cursor()
cur.execute(f"INSERT INTO members VALUES (?, ?);", (rfid, name))