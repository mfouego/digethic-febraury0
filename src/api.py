import pickle
from flask import Flask, request
import pandas as pd  # noqa
import os  # noqa
from flask_cors import CORS
import numpy as np  # noqa
from werkzeug import Response
from io import StringIO


app = Flask(__name__)

CORS(app)


training_data = pd.read_csv(os.path.join('data', "auto-mpg-training-data.csv"))

file_to_open = open(os.path.join(
    'data', 'models', "baummethoden_lr.pickle"), 'rb')
trained_model = pickle.load(file_to_open)
file_to_open.close()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")


@app.route("/predict", methods=["GET"])
def predict():
    zylinder = request.args.get('zylinder')
    ps = request.args.get('ps')
    gewicht = request.args.get('gewicht')
    beschleunigung = request.args.get('beschleunigung')
    baujahr = request.args.get('baujahr')

    csv_string = ",".join([zylinder, ps, gewicht, beschleunigung, baujahr])

    csv_data = StringIO(csv_string)
    attribute_names = [zylinder, ps, gewicht, beschleunigung, baujahr]
    prediction_data = pd.read_csv(csv_data, names=attribute_names)
    prediction = trained_model.predict(prediction_data)

    print(prediction)
    return{"result": prediction[0]}

    # prediction = trained_model.predict(
    #   [[zylinder, ps, gewicht, beschleunigung, baujahr]])
    # print(prediction)
    # return {"result": prediction[0]}
