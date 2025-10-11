import sqlite3

DB_FILE = "routes.db"

def print_all_routes():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, route_no, start_junction, end_junction, status, created_at FROM routes ORDER BY id")
    rows = cur.fetchall()
    if not rows:
        print("⚠️ No routes found.")
    else:
        print("✅ Routes in DB:\n")
        for r in rows:
            print(f"ID: {r[0]} | Route No: {r[1]} | {r[2]} -> {r[3]} | Status: {r[4]} | Created: {r[5]}")
    conn.close()

def print_latest_route():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT route_no FROM routes ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()
    if row:
        print("\nLatest Route Number:", row[0])
    else:
        print("⚠️ No routes found.")
    conn.close()

if __name__ == "__main__":
    print_all_routes()
    print_latest_route()

