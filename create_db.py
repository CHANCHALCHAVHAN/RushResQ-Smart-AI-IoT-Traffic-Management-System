import sqlite3
from datetime import datetime

# Create database file
conn = sqlite3.connect("routes.db")
cur = conn.cursor()

