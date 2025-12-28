import json
import csv
from io import StringIO
from .database import connect

def export_json(printer: str):
    with connect() as db:
        usage = db.execute(
            "SELECT * FROM usage WHERE printer=?",
            (printer,)
        ).fetchone()

        maintenance = db.execute(
            "SELECT task, interval, last_reset FROM maintenance WHERE printer=?",
            (printer,)
        ).fetchall()

    return {
        "printer": printer,
        "usage": {
            "total_print_seconds": usage[1],
            "total_power_seconds": usage[2]
        },
        "maintenance": [
            {
                "task": t,
                "interval_hours": i,
                "last_reset_hours": r
            }
            for t, i, r in maintenance
        ]
    }

def export_csv(printer: str):
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["task", "interval_hours", "last_reset_hours"])

    with connect() as db:
        rows = db.execute(
            "SELECT task, interval, last_reset FROM maintenance WHERE printer=?",
            (printer,)
        ).fetchall()

    for row in rows:
        writer.writerow(row)

    return output.getvalue()
