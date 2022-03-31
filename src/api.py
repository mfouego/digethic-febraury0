from flask import Flask

import pandas as pd  # noqa
import os  # noqa
from flask_cors import CORS

from werkzeug import Response

app = Flask(__name__)

CORS(app)

# training_data = data = pd.read_csv('data\auto-mpg-training-data.csv', sep=";")
# print(data)
training_data = pd.read_csv(os.path.join('data', "auto-mpg-training-data.csv"))

print(training_data)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")
