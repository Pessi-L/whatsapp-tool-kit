from flask import Flask
from flask import request
from twilio.rest import Client
import os

app = Flask(__name__)

ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_NUMBER = 'whatsapp:+14155238886'
# initializing a client
client = Client(ACCOUNT_ID, TWILIO_TOKEN)


def process_message(msg):
    if msg == 'hi':
        return 'Welcome to WhatsApp tool kit!'
    else:
        return 'Please type "hi" to get started'


def send_message(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )


@app.route('/webhook', methods=['POST'])
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_message(msg)
    send_message(response, sender)

    return 'OK', 200

