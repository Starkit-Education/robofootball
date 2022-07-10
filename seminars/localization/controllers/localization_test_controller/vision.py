import math
import json
 
class Vision():
    def __init__(self, camera, robot, landmarks = "landmarks.json"):
        self.camera = camera
        self.robot = robot
        with open(landmarks, "r") as file:
            self.posts = json.load(file)


    def get_position(self, positions):
        xy_robot = self.robot.getSelf().getPosition()
        xt = positions[0] - xy_robot[0]
        yt = positions[1] - xy_robot[1]
        angle = self.return_angle()
        x = xt*math.cos(angle) - yt*math.sin(angle)
        y = xt*math.sin(angle) + yt*math.cos(angle)
        return [x, y]

    def check_angle(self):
        angle = self.robot.getSelf().getProtoField("rotation").getSFRotation()[3]
        if abs(angle ) < math.pi/2:
            return True
        else:
            return False

    def return_angle(self):
        return self.robot.getSelf().getProtoField("rotation").getSFRotation()[3]

    def update(self):
        results = {}
        objects = self.camera.getRecognitionObjects()
        if self.check_angle():
            posts = self.posts["blue_posts"]
            results.update({"blue_posts":[]})
            post_color = "blue_posts"
        else:
            posts = self.posts["yellow_posts"]
            results.update({"yellow_posts":[]})
            post_color = "yellow_posts"
        
        if len(objects) > 0:
            for obj in objects:
                if obj.get_model().decode("utf-8") == "left post":
                    results[post_color].append(self.get_position(self.posts[post_color][0]))
                elif obj.get_model().decode("utf-8") == "right post":
                    results[post_color].append(self.get_position(self.posts[post_color][1]))
                
        return results
            