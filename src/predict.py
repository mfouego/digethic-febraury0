import pandas as pd
import pickle

file_to_open = open("data/models/baummethoden_lr.pickle", "rb")
trained_model = pickle.load(file_to_open)
file_to_open.close()

prediction_data = pd.read_csv('data/prediction-training-data.csv', sep=";")
print(prediction_data)
print(trained_model.predict(prediction_data))
