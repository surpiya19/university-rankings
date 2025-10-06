import sqlite3

try:
    conn = sqlite3.connect("data/university_database.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Connected successfully. Tables:", cur.fetchall())
    conn.close()
except Exception as e:
    print("Connection failed:", e)
