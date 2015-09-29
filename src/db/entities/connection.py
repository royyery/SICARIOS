__author__ = 'Ariel'
import sqlite3
from pathlib import Path

# class to connect the database
def connection():
    database = sqlite3.connect("C:\Users\Ariel\Documents\SicariosRepo\src\db\entities")
    return database
