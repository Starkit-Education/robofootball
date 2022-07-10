import json
import math
import sys

sys.path.append("filter/")

from ParticleFilter import ParticleFilter
from robot import Robot
from field import Field



class Localization():
    def __init__(self, landmarks = "landmarks.json"):
        with open(landmarks, "r") as file:
            self.landmarks = json.load(file)
        self.position = ()
        self.particle_filter = ParticleFilter(Robot(0.0, 0.0, 0.0), Field("filter/parfield.json"), self.landmarks, n = 1000, apr = True)

    def update(self, mesurements):
        
        self.position = self.particle_filter.update_particle_filter(mesurements)

        #self.position = (self.particle_filter.return_coord())
        """
        Здесь будет ваш код
        В переменной mesurements лежат данные о положении стоек в локальной системе координат робота
        """
        pass

    def return_position(self):
        return self.position
        