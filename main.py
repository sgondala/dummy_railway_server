# # A simple webserver to handle few get and post requests

# from flask import Flask, request
# import os

# # On Heroku, the port is set in the environment variable PORT
# # Listen on 0.0.0.0

# app = Flask(__name__)


# @app.route('/get', methods=['GET'])
# def get():
#     return "GET request received"

# # Post method expects a json object
# @app.route('/process_email/', methods=['POST'])
# def post():
#     data = request.get_json()
#     print(data)
#     return "POST request received"

# if __name__ == '__main__':
#     # Run app on 0.0.0.0
#     # Pick port from osenv PORT or default to 5000
#     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
