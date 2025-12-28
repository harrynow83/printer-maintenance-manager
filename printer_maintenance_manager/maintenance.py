from .database import connect
from .usage import get_stats
from .config import MAINTENANCE_TASKS

def ensure_tasks(printer):
    with connect() as db:
        for task, hours in MAINTENANCE_TASKS.items():
            db.execute("""
            INSERT OR IGNORE INTO maintenance
            (printer, task, interval, last_reset)
            VALUES (?, ?, ?, 0)
            """, (printer, task, hours))

def check(printer):
    ensure_tasks(printer)
    stats = get_stats(printer)
    due = []

    with connect() as db:
        for task, interval, last_reset in db.execute("""
            SELECT task, interval, last_reset
            FROM maintenance WHERE printer=?
        """, (printer,)):
            if stats["print_hours"] - last_reset >= interval:
                due.append(task)

    return due, stats["print_hours"]

def reset(printer, task, current_hours):
    with connect() as db:
        db.execute("""
        UPDATE maintenance
        SET last_reset=?
        WHERE printer=? AND task=?
        """, (current_hours, printer, task))
