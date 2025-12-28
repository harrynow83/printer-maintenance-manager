from .telegram import send_telegram

def send_alert(message: str):
    """
    Send alert message to all enabled alert providers.
    """
    # Por ahora solo Telegram
    send_telegram(message)
