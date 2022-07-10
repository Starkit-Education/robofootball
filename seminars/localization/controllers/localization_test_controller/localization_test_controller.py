from controller import Robot, Supervisor
from localization import Localization
from vision import Vision

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

localization = Localization()

camera = robot.getDevice('camera')
camera.enable(timestep)
camera.recognitionEnable(timestep)
vision = Vision(camera, robot)


while robot.step(32) != -1:
    mesurements = vision.update()
    localization.update(mesurements)
    print(localization.return_position())