from flask import Flask
from app.webhook_whatsapp import webhook
import os

app = Flask(__name__)
app.register_blueprint(webhook)

@app.route('/')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
