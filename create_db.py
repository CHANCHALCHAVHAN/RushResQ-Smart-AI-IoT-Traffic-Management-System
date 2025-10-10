import sqlite3
from datetime import datetime

# Create database file
conn = sqlite3.connect("routes.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_no TEXT NOT NULL,
    start_junction TEXT,
    end_junction TEXT,
    status TEXT,
    created_at TEXT
)
""")

