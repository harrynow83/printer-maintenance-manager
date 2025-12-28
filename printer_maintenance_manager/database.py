import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "printer_data" / "maintenance_manager.db"

def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db(printer):
    with connect() as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS usage (
            printer TEXT PRIMARY KEY,
            total_print INTEGER DEFAULT 0,
            total_power INTEGER DEFAULT 0,
            last_print REAL,
            last_power REAL
        )
        """)
        db.execute("""
        CREATE TABLE IF NOT EXISTS maintenance (
            printer TEXT,
            task TEXT,
            interval INTEGER,
            last_reset REAL,
            PRIMARY KEY (printer, task)
        )
        """)
        db.execute("""
        INSERT OR IGNORE INTO usage (printer)
        VALUES (?)
        """, (printer,))
