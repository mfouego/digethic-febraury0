from flask import Flask
import pandas as pd  # noqa
import os  # noqa
from flask_cors import CORS
from markupsafe import escape  # noqa

app = Flask(__name__)

CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/", methods=["GET"])
def index():
    return {"Hello": "World"}
