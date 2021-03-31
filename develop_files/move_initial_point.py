from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord, Angle, Coord
import time

speed = 20
mycobot = MyCobot('COM6')

mycobot.send_coords([160, 160, 140, 45, 55, 40], speed, 0)
time.sleep(1)
print(mycobot.get_coords())