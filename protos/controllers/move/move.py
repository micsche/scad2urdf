"""move controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
TIME_STEP = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
# create the Robot instance.


# get the motor devices
leftMotor = robot.getMotor('hip2rightthigh')
rightMotor = robot.getMotor('hip2leftthigh')
# set the target position of the motors

x=0

while robot.step(TIME_STEP) != -1:
    leftMotor.setPosition(x)
    rightMotor.setPosition(-x)
    
    x=x+0.01
    print(x)
    pass