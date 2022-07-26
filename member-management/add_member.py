import sqlite3
import sys
from unicodedata import name

con = sqlite3.connect(sys.argv[0] + "/../members.db")
cur = con.cursor()
# @cmilbert: please store data and id from a scanned rfid tag in variables here.
cur.execute(f"INSERT INTO members({id}, {name})")