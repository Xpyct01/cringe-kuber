from flask import Flask
import os
import json


app = Flask(__name__)


@app.route("/")
def predict():
    username = os.environ['SECRET_USERNAME']
    return {"username": username}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
