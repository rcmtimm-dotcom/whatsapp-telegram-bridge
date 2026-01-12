import requests
from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_to_telegram(valor, categoria):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': f"💰 Gasto registrado\nValor: R${valor}\nCategoria: {categoria}"
    }
    r = requests.post(url, json=payload, timeout=10)
    r.raise_for_status()
