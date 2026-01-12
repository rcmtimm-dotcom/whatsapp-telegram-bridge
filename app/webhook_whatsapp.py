from flask import Blueprint, request
from app.parser import parse_message
from app.telegram_client import send_to_telegram
from app.config import ALLOWED_GROUP_JID

webhook = Blueprint('webhook', __name__)

@webhook.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    data = request.json or {}

    try:
        message = data['message']['conversation']
        group_jid = data['key']['remoteJid']
    except Exception:
        return ('', 200)

    if ALLOWED_GROUP_JID and group_jid != ALLOWED_GROUP_JID:
        return ('', 200)

    parsed = parse_message(message)
    if not parsed:
        return ('', 200)

    valor, categoria = parsed
    send_to_telegram(valor, categoria)
    return ('', 200)
