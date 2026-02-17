import sqlite3

DB_NAME = "tallyroom.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    create_tables(conn)
    return conn

def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        note TEXT
    )
    """)
    conn.commit()
