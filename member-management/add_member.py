import sqlite3
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
scanned = False
while scanned is False:
    print("Scan member card.")
    rfid, name = reader.read()
    scanned = True
con = sqlite3.connect(sys.argv[0] + "/../members.db")
cur = con.cursor()
cur.execute(f"INSERT INTO members({rfid}, {name})")