from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord, Angle, Coord
import time

mycobot = MyCobot('COM6')

print('Joint Angle' )
print('[  J1,  J2,  J3,  J4,  J5,  J6] (deg)' )
print(mycobot.get_angles())
print('\n' )
print('Coords')
print('[  X,  Y,  Z,  RX,  RY,  RZ] ' )
print(mycobot.get_coords())