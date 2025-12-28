import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.yaml"

# Defaults (si el archivo no existe o está incompleto)
TELEGRAM_ENABLED = False
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""

MAINTENANCE_TASKS = {
    "nozzle_clean": 100,
    "belts_check": 300,
    "lubrication": 500,
    "hotend_overhaul": 1000
}


def load_config():
    global TELEGRAM_ENABLED
    global TELEGRAM_BOT_TOKEN
    global TELEGRAM_CHAT_ID
    global MAINTENANCE_TASKS

    if not CONFIG_PATH.exists():
        return

    with open(CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f) or {}

    # ---- Alerts ----
    alerts = data.get("alerts", {})
    telegram = alerts.get("telegram", {})

    TELEGRAM_ENABLED = telegram.get("enabled", TELEGRAM_ENABLED)
    TELEGRAM_BOT_TOKEN = telegram.get("bot_token", TELEGRAM_BOT_TOKEN)
    TELEGRAM_CHAT_ID = telegram.get("chat_id", TELEGRAM_CHAT_ID)

    # ---- Maintenance ----
    MAINTENANCE_TASKS = data.get("maintenance", MAINTENANCE_TASKS)
