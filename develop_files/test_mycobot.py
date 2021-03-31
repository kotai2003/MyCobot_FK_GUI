from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord, Angle, Coord
import time

import serial
#
# ser = serial.Serial('COM6',9600)
# print(ser.name)
#
#
mycobot = MyCobot('COM6')
mycobot.power_on()
# mycobot.set_free_mode()
mycobot.send_angles([0,0,0,0,0,0],20)
time.sleep(5)
# mycobot.send_angle(Angle.J2.value, 15, 30)
# mycobot.send_coord(Coord.X.value, -40,70)
mycobot.send_angles([45,45,45,45,45,45],10)
time.sleep(3)
mycobot.send_angles([60,60,60,60,60,60],10)
time.sleep(3)
mycobot.send_angles([0,0,0,0,0,0],50)

mycobot.set_led_color('ff00ff')
a = mycobot.get_angles()
print(type(a))
print(a)


# mycobot.send_coord(Coord.X.value,-40,70)
# mycobot.send_angle(Angle.J2.value, 10, 50)