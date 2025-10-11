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

# Insert some sample rows
sample = [
    ("R001", "JUNC_10", "JUNC_13", "active", datetime.now().isoformat()),
    ("R002", "JUNC_14", "JUNC_17", "inactive", datetime.now().isoformat()),
    ("R003", "JUNC_20", "JUNC_22", "active", datetime.now().isoformat()),
]

cur.executemany(
    "INSERT INTO routes (route_no, start_junction, end_junction, status, created_at) VALUES (?, ?, ?, ?, ?)", 
    sample
)

conn.commit()
conn.close()

print("✅ Database created and sample rows inserted into routes.db")

