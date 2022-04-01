from io import StringIO
import pandas as pd
from flask import Flask, response
zylinder = request.args.get('zylinder')
ps = request.args.get('ps')
gewicht = request.args.get('gewicht')
beschleunigung = request.args.get('beschleunignung')
baujahr = request.args.get('baujahr')

csv_string = ",".join([zylinder, ps, gewicht, beschleunignung, baujahr])

csv_data = StringIO(csv_string)
attribute_names = [zylinder, ps, gewicht, beschleunignung, baujahr]
prediction_data = pd.read_csv(csv_data, names=attribute_names)
prediction = trained_model.predict(prediction_data)
