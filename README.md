
# MyCobot_FK_GUI
GUI Program to control the MyCobot. 
This is simulating the movement of the mycobot by Forward Kinematics. That is why this repositry is called MyCobot_*FK*_GUI. 
You can control MyCobot with chainging joint angle and speed. 

This work is inspired by @Robonchu 's amazing work
https://github.com/Robonchu/PythonSimpleManipulation

# DEMO

![screen](https://user-images.githubusercontent.com/11495016/113101415-a724de80-9237-11eb-8a22-09c787c3420a.jpg)
https://user-images.githubusercontent.com/11495016/113101260-7644a980-9237-11eb-8710-bd71e688abc8.mp4

![screen02](https://user-images.githubusercontent.com/11495016/113101628-ea7f4d00-9237-11eb-9c3d-092ac4f5f1a5.jpg)
https://user-images.githubusercontent.com/11495016/113101269-780e6d00-9237-11eb-8fb1-31c26610014f.mp4


# Features
1. Well-designed GUI Design is prepared.
2. You can check the position of the robot arm and end-effector with 3D display.
3. You can change the 6 joint angles and speed of motor with slider bars.
4. Home and Random position buttons are prepared.
5. Robot arm will start to move by clicking 'Execute' button, 

# Requirement
python
Pillow
numpy 
matplotlib
tkinter
pymycobot

# Installation
```
git clone https://github.com/kotai2003/MyCobot_FK_GUI.git
```

# Usage
```
python GUI-MyCobot-Forward-Kinetics-controller-rev02.py
```

# Note
You need to change the device name according to your system settings.
please open the GUI-MyCobot-Forward-Kinetics-controller-rev02.py and go to the line 18.
you will find the follwing line.
```
device_name = 'COM6'
```
1. if your myCobot is connected to 'COM3' on Windows system.
```python
device_name = 'COM3'
```
2. if your myCobot is connected to USB on Linux system.
```python
device_name = '/dev/ttyusb0'
```

# Author

*Name: S Choe

*Affilitation : Tomomi Research Inc. (https://www.tomomi-research.com)

*twitter : @wireless_power (https://www.twitter.com/wireless_power)

# License

Mycobot_FK_GUI is under  [MIT license](https://en.wikipedia.org/wiki/MIT_License).
