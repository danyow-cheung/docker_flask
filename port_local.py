import requests
from flask import Flask

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello from Flask App 2!'

@app.route('/send')
def send_message():
    response = requests.get('http://port5000:8000/message')
    message = response.json().get('message')
    return 'Received message from Flask App 1: ' + message

if __name__ == '__main__':
    app.run(port=1245)