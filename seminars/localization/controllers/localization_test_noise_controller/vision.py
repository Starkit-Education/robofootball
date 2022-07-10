import math
import json
from os import X_OK
import random

class Vision():
    def __init__(self, camera, robot, landmarks = "landmarks.json"):
        self.camera = camera
        self.robot = robot
        with open(landmarks, "r") as file:
            self.posts = json.load(file)

    def get_random_position(self):
        A = 6
        B = 4
        x = A + 2*random.random()
        y = B + 2*random.random()
        return [x, y]

    def get_position(self, positions):
        xy_robot = self.robot.getSelf().getPosition()
        xt = positions[0] - xy_robot[0]
        yt = positions[1] - xy_robot[1]
        angle = self.return_angle()
        x = xt*math.cos(angle) - yt*math.sin(angle) + random.gauss(0, 0.03)
        y = xt*math.sin(angle) + yt*math.cos(angle) + random.gauss(0, 0.03)
        return [x, y]

    def check_angle(self):
        angle = self.robot.getSelf().getProtoField("rotation").getSFRotation()[3]
        if abs(angle ) < math.pi/2:
            return True
        else:
            return False

    def return_angle(self):
        return self.robot.getSelf().getProtoField("rotation").getSFRotation()[3]

    def update(self, mesurements):
        results = {}
        post_color = "blue_posts"
        objects = self.camera.getRecognitionObjects()
        if self.check_angle() and len(mesurements)==0:
            posts = self.posts["blue_posts"]
            mesurements.update({"blue_posts":{"left post":[],"right post":[]}})
            post_color = "blue_posts"
        elif not self.check_angle() and len(mesurements)==0:
            posts = self.posts["yellow_posts"]
            mesurements.update({"yellow_posts":{"left post":[],"right post":[]}})
            post_color = "yellow_posts"
        
        if len(objects) > 0:
            for obj in objects:
                if obj.get_model().decode("utf-8") == "left post":
                    mesurements[post_color]["left post"].append(self.get_position(self.posts[post_color][0]))
                    if random.random() < 0.2:
                        mesurements[post_color]["left post"].append(self.get_random_position())
                elif obj.get_model().decode("utf-8") == "right post":
                    mesurements[post_color]["right post"].append(self.get_position(self.posts[post_color][1]))
                    if random.random() < 0.2:
                        mesurements[post_color]["right post"].append(self.get_random_position())
        return mesurements
            