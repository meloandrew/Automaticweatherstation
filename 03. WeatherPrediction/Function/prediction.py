import pickle
# import numpy as np
class Predict():
    def __init__(self):
        pass

    def run(self, temperature: float, humidity: float, wind_velocity: float, pressure: float) -> int:
        model = pickle.load(open("Function\modelo_rf.sav", "rb"))
        arr = [[temperature, humidity, pressure, wind_velocity]]
        predict: int = model.predict(arr)[0]
        return predict.item()
    pass
