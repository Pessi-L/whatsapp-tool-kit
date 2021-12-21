from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return {
        'Result': 'Welcome to WhatsApp tool kit!'
    }
