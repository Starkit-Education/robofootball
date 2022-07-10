import math


class Robot:
    def __init__(self, x=0, y=0, yaw=0):
        self.x = x          # robot's x coordinate
        self.y = y          # robot's y coordinate
        self.yaw = yaw      # robot's angle

    def set_coord(self, new_x, new_y, new_orientation):
        self.x = float(new_x)
        self.y = float(new_y)
        self.yaw = float(new_orientation)

    def sense(self, landmarks):
        z = []
        for i in range(len(landmarks)):
            dist = math.sqrt((self.x - landmarks[i][0]) ** 2
                             + (self.y - landmarks[i][1]) ** 2)
            z.append(dist)
        return z

    def move(self, x, y, yaw):
        # turn, and add randomomness to the turning command
        orientation = self.yaw + float(yaw)
        if orientation < 0:
            orientation += (math.pi*2)
        orientation %= (2 * math.pi)
        self.x += x*math.cos(self.yaw)
        self.y += x*math.sin(self.yaw)
        self.yaw = orientation

    def observation_to_predict(self, observations, landmarks):
        predicts = []
        for color_landmarks in landmarks:
            if (color_landmarks not in landmarks):
                continue

            for landmark in landmarks[color_landmarks]:
                x_posts = self.x - \
                    observation[0]*math.sin(-self.yaw) + \
                    observation[1]*math.cos(-self.yaw)
                y_posts = self.y + \
                    observation[0]*math.cos(-self.yaw) - \
                    observation[1]*math.sin(-self.yaw)
                predicts.append([x_posts, y_posts])
        return predicts