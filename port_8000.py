from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello from Flask App 1!'

@app.route('/message')
def get_message():
    return jsonify(message='This is a message from Flask App 1.')

if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0")