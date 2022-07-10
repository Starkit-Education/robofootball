import json
import math

class Localization():
    def __init__(self, landmarks = "landmarks.json"):
        with open(landmarks, "r") as file:
            self.landmarks = json.load(file)
        self.position = ()

    def update(self, mesurements):
        
        """
        Здесь будет ваш код
        В переменной mesurements лежат данные о положении стоек в локальной системе координат робота
        """
        pass

    def return_position(self):
        return self.position
        