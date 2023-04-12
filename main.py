# A simple webserver to handle few get and post requests

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    return "GET request received"

# Post method expects a json object
@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    print(data)
    return "POST request received"

if __name__ == '__main__':
    app.run(debug=True)