from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord, Angle, Coord
import time

import serial
#
# ser = serial.Serial('COM6',9600)
# print(ser.name)
#
speed = 70
mycobot = MyCobot('COM6')
#Initinalize

mycobot.power_on()
mycobot.send_angles([0,0,0,0,0,0],speed)
print(mycobot.is_in_position(data=[0,0,0,0,0,0], id=0))
# time.sleep(1)
# print(mycobot.get_coords())
# time.sleep(1)
# print(mycobot.get_coords())
# time.sleep(1)
# print(mycobot.get_coords())
time.sleep(5)
print(mycobot.get_angles())
time.sleep(5)
print(mycobot.get_angles())
print(mycobot.is_in_position(data=[0,0,0,0,0,0], id=0))

# #Coord
# coords = mycobot.get_coords()
# print('coords', coords)
#
# mycobot.send_coords([160, 160, 160, 45, 45, 45], 70, 0)
# print(mycobot.is_paused())
# print(mycobot.is_moving())
#
#
# #z
# coords[2] = coords[2] - 50
# mycobot.send_coords(coords, speed = angle_speed, mode = 0)
# time.sleep(3)
# #x
# coords[4] = coords[4] + 200
# mycobot.send_coords(coords, speed = angle_speed, mode = 0)
# time.sleep(3)
#
#
# mycobot.set_free_mode()

# mycobot.send_angles([50,30,20,30,10,10],angle_speed)
# # mycobot.set_free_mode()
#
# time.sleep(5)
# # mycobot.send_angle(Angle.J2.value, 15, 30)
# # mycobot.send_coord(Coord.X.value, -40,70)
# mycobot.send_angles([45,45,45,45,45,45],10)
# time.sleep(3)
# mycobot.send_angles([60,60,60,60,60,60],10)
# time.sleep(3)
# mycobot.send_angles([0,0,0,0,0,0],50)
#
# mycobot.set_led_color('ff00ff')
# a = mycobot.get_angles()
# print(type(a))
# print(a)
#
#
# # mycobot.send_coord(Coord.X.value,-40,70)
# # mycobot.send_angle(Angle.J2.value, 10, 50)