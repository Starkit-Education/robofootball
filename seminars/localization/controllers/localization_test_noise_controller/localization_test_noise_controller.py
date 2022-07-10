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

while True:
    mesurements = {}
    for i in range(5):
        robot.step(32)
        mesurements = vision.update(mesurements)
    localization.update(mesurements)  
    print(localization.return_position())
    robot.step(32)