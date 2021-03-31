from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord, Angle, Coord
import time

speed = 20
mycobot = MyCobot('COM6')

mycobot.send_angles([0,0,0,0,0,0],speed)

print(mycobot.get_angles())
print(mycobot.get_speed())
print(mycobot.get_joint_min_angle(6))
print(mycobot.get_joint_max_angle(6))
