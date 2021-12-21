from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return {
        'Result': 'Welcome to whatsapp tool kit!'
    }
