import math
import sys

import random 
from robot import Robot


def gaussian(x, sigma):
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return math.exp(-(x ** 2) / 2*(sigma ** 2)) / math.sqrt(2.0 * math.pi * (sigma ** 2))

class Particle(Robot):
    
    def observation_score(self, observations, landmarks, sense_noise):
        # particle weight calculation
        prob = 1.0
        for color_landmarks in observations:
            if (color_landmarks not in landmarks):
                continue

            for landmark in landmarks[color_landmarks]:
                dists = []
                if observations[color_landmarks]:

                    for observation in observations[color_landmarks]:
                        # calc posts coords in field for every mesurement
                        x_posts = self.x + \
                            observation[0]*math.cos(self.yaw) - \
                            observation[1]*math.sin(self.yaw)
                        y_posts = self.y + \
                            observation[0]*math.sin(self.yaw) + \
                            observation[1]*math.cos(self.yaw)
                        dist = math.sqrt(
                            (x_posts - landmark[0])**2 + (y_posts - landmark[1])**2)
                        dists.append(dist)
                if (dists != []):
                    prob *= gaussian(min(dists), sense_noise)
        return prob
