from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    response = jsonify({"Choo Choo": "Welcome to your  Flask app 🚅"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
