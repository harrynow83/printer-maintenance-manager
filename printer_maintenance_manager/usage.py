import time
from .database import connect

def power_on(printer):
    with connect() as db:
        db.execute(
            "UPDATE usage SET last_power=? WHERE printer=?",
            (time.time(), printer)
        )

def power_off(printer):
    with connect() as db:
        cur = db.execute(
            "SELECT last_power FROM usage WHERE printer=?",
            (printer,)
        )
        last = cur.fetchone()[0]
        if last:
            db.execute("""
            UPDATE usage
            SET total_power = total_power + ?,
                last_power = NULL
            WHERE printer=?
            """, (time.time() - last, printer))

def print_start(printer):
    with connect() as db:
        db.execute(
            "UPDATE usage SET last_print=? WHERE printer=?",
            (time.time(), printer)
        )

def print_end(printer):
    with connect() as db:
        cur = db.execute(
            "SELECT last_print FROM usage WHERE printer=?",
            (printer,)
        )
        last = cur.fetchone()[0]
        if last:
            db.execute("""
            UPDATE usage
            SET total_print = total_print + ?,
                last_print = NULL
            WHERE printer=?
            """, (time.time() - last, printer))

def get_stats(printer):
    with connect() as db:
        p, pw = db.execute(
            "SELECT total_print, total_power FROM usage WHERE printer=?",
            (printer,)
        ).fetchone()
    return {
        "print_hours": round(p / 3600, 2),
        "power_hours": round(pw / 3600, 2)
    }
