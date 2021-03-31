import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
from Robonchu_module.ForwardKinetics import *
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
import time
import random

#My Cobot

device_name = 'COM6'
mycobot = MyCobot(device_name)
state_LED = False



#Robot Information
# Link Length
L1 = [0., 0., 0.06114]
L2 = [0., 0., 0.07042]
L3 = [0., 0., 0.1104]
L4 = [0., 0., 0.0960]
L5 = [0., 0.06639, 0.]
L6 = [0., 0., 0.07318]
L7 = [-0.0436, 0., 0.]
LINK_LENGTHS = np.array([L1, L2, L3, L4, L5, L6, L7])


# Joint Vector
J1 = [0, 0, 1]
J2 = [0, 1, 0]
J3 = [0, 1, 0]
J4 = [0, 1, 0]
J5 = [0, 0, 1]
J6 = [1, 0, 0]
J7 = [0, 0, 0]
JOINT_VECTORS = np.array([J1, J2, J3, J4, J5, J6, J7])



class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)


        self.master.geometry("1000x850")
        self.master.title("MyCobot Forward Kinetics")
        self.master.resizable(True, True)
        self.pack()

        # ---------------------------------------
        # Favicon
        # ---------------------------------------
        self.iconfile = './image/favicon.ico'
        self.master.iconbitmap(default = self.iconfile)


        # --------------------------------------------------------------
        # Font
        # ---------------------------------------------------------------
        self.font_frame = font.Font(family = "Meiryo UI", size = 15, weight = "normal")

        self.font_btn_big = font.Font(family = "Meiryo UI", size = 20, weight = "bold")
        self.font_btn_small = font.Font(family = "Meiryo UI", size = 15, weight = "bold")

        self.font_lbl_bigger = font.Font(family = "Meiryo UI", size = 45, weight = "bold")
        self.font_lbl_big = font.Font(family = "Meiryo UI", size = 30, weight = "bold")
        self.font_lbl_middle = font.Font(family = "Meiryo UI", size = 15, weight = "bold")
        self.font_lbl_small = font.Font(family = "Meiryo UI", size = 12, weight = "normal")

        self.create_widgets()
        self._set_var()
        self._calc_angle()



# --------------------------------------------------------
#  Tkinter Widget
# --------------------------------------------------------

    def create_widgets(self):
        #########################################
        # Tab
        #########################################

        self.tabControl = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text = 'Operation')
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text = 'Config')
        self.tabControl.pack(expand = 1, fill = "both")

        #########################################
        # Frame : Logo and Title @tab1
        #########################################
        self.frame_logo = ttk.Frame(self.tab1)
        self.frame_logo.configure(width = 1000, height = 100)
        self.frame_logo.place(x = 5, y = 5)
        self.frame_logo.grid_propagate(0)

        # ----------------------------------------
        # Logo Image
        # ----------------------------------------
        self.logo_img = Image.open('image/Logo_Small_new.png')
        self.logo_img = self.logo_img.resize((182, 57))
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.cav_logo = tk.Canvas(self.frame_logo, width = 182, height = 57)
        self.cav_logo.create_image(5, 5, image = self.logo_img, anchor = 'nw')
        self.cav_logo.grid(column = 0, row = 0, padx = 10, pady = 10)

        #########################################
        # Frame for  Canvas
        #########################################
        self.frame_canvas = tk.LabelFrame(self.tab1, text='Canvas')
        self.frame_canvas.configure(width = 650, height = 620)
        self.frame_canvas.place(x = 5, y = 100)
        self.frame_canvas.grid_propagate(0)

        #----------------------------------------
        # Canvas
        # ----------------------------------------
        self.canvas = FigureCanvasTkAgg(fig, self.frame_canvas)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame_canvas)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

        #########################################
        # Frame : Emergency Control
        #########################################
        self.frame_control = tk.LabelFrame(self.tab1, text = 'Control')
        self.frame_control.configure(width = 975, height = 80)
        self.frame_control.place(x = 5, y = 710)
        self.frame_control.grid_propagate(0)

        # ----------------------------------------
        # Speed Setting
        # ----------------------------------------
        ss_length = 100
        self.lbl_SS = tk.Label(self.frame_control, text = 'Speed', font = self.font_lbl_middle)
        self.lbl_SS.grid(column = 0, row = 0, padx = 10, pady = 0)

        self.val_SS = tk.IntVar()
        self.scale_SS = tk.Scale(self.frame_control)
        self.scale_SS.configure(orient = 'horizontal', font = self.font_lbl_small, length = ss_length)
        self.scale_SS.configure(from_ = 0, to = 100, resolution = 10)
        self.scale_SS.configure(variable = self.val_SS)
        self.scale_SS.grid(column = 1, row = 0, padx = 10, pady = 0)

        # ----------------------------------------
        # Emergency Stop
        # ----------------------------------------
        self.btn_Stop = tk.Button(self.frame_control, text = 'Stop', fg='red')
        self.btn_Stop.configure(font = self.font_btn_small, width = 10, command = self._stop_myCobot)
        self.btn_Stop.grid(column = 2, row = 0, padx = 10, pady = 0)

        # ----------------------------------------
        # Release Robot
        # ----------------------------------------
        self.btn_Release = tk.Button(self.frame_control, text = 'Release', fg = 'red')
        self.btn_Release.configure(font = self.font_btn_small, width = 10, command = self._release_myCobot)
        self.btn_Release.grid(column = 3, row = 0, padx = 10, pady = 0)

        # ----------------------------------------
        # Flash LED
        # ----------------------------------------
        self.btn_LED = tk.Button(self.frame_control, text = 'LED', fg='blue')
        self.btn_LED.configure(font = self.font_btn_small, width = 10, command = self._flash_LED)
        self.btn_LED.grid(column = 4, row = 0, padx = 10, pady = 0)


        #########################################
        # Frame : Button
        #########################################
        self.frame_button = tk.LabelFrame(self.tab1, text='Button')
        self.frame_button.configure(width = 300, height = 610)
        self.frame_button.place(x = 680, y = 100)
        self.frame_button.grid_propagate(0)



        #----------------------------------------
        # Scale 1. : Joint 1
        #----------------------------------------
        scale_length = 150
        self.lbl_A = tk.Label(self.frame_button, text = 'Joint 1', font = self.font_lbl_middle)
        self.lbl_A.grid(column = 0, row = 0, padx = 10, pady = 10)

        self.val_A = tk.DoubleVar()
        self.scale_A = tk.Scale(self.frame_button)
        self.scale_A.configure(orient = 'horizontal', font = self.font_lbl_small, length = scale_length,command=self._calc_angle)
        self.scale_A.configure(from_ = -160, to = 160, resolution = 1)
        self.scale_A.configure(variable = self.val_A)
        self.scale_A.grid(column = 1, row = 0, padx = 10, pady = 10)

        #----------------------------------------
        # Scale 2. : Joint 2
        #----------------------------------------

        self.lbl_B = tk.Label(self.frame_button, text = 'Joint 2', font = self.font_lbl_middle)
        self.lbl_B.grid(column = 0, row = 1, padx = 10, pady = 10)

        self.val_B = tk.DoubleVar()
        self.scale_B = tk.Scale(self.frame_button)
        self.scale_B.configure(orient = 'horizontal', font = self.font_lbl_small, length = scale_length,command=self._calc_angle)
        self.scale_B.configure(from_ = -160, to = 160, resolution = 1)
        self.scale_B.configure(variable = self.val_B)
        self.scale_B.grid(column = 1, row = 1, padx = 10, pady = 10)

        # ----------------------------------------
        # Scale 3. : Joint 3
        # ----------------------------------------

        self.lbl_C = tk.Label(self.frame_button, text = 'Joint 3', font = self.font_lbl_middle)
        self.lbl_C.grid(column = 0, row = 2, padx = 10, pady = 10)

        self.val_C = tk.DoubleVar()
        self.scale_C = tk.Scale(self.frame_button)
        self.scale_C.configure(orient = 'horizontal', font = self.font_lbl_small, length = scale_length,
                               command = self._calc_angle)
        self.scale_C.configure(from_ = -160, to = 160, resolution = 1)
        self.scale_C.configure(variable = self.val_C)
        self.scale_C.grid(column = 1, row = 2, padx = 10, pady = 10)

        # ----------------------------------------
        # Scale 4. : Joint 4
        # ----------------------------------------

        self.lbl_D = tk.Label(self.frame_button, text = 'Joint 4', font = self.font_lbl_middle)
        self.lbl_D.grid(column = 0, row = 3, padx = 10, pady = 10)

        self.val_D = tk.DoubleVar()
        self.scale_D = tk.Scale(self.frame_button)
        self.scale_D.configure(orient = 'horizontal', font = self.font_lbl_small, length = scale_length,
                               command = self._calc_angle)
        self.scale_D.configure(from_ = -160, to = 160, resolution = 1)
        self.scale_D.configure(variable = self.val_D)
        self.scale_D.grid(column = 1, row = 3, padx = 10, pady = 10)

        # ----------------------------------------
        # Scale 5. : Joint 5
        # ----------------------------------------

        self.lbl_E = tk.Label(self.frame_button, text = 'Joint 5', font = self.font_lbl_middle)
        self.lbl_E.grid(column = 0, row = 4, padx = 10, pady = 10)

        self.val_E = tk.DoubleVar()
        self.scale_E = tk.Scale(self.frame_button)
        self.scale_E.configure(orient = 'horizontal', font = self.font_lbl_small, length = scale_length,
                               command = self._calc_angle)
        self.scale_E.configure(from_ = -160, to = 160, resolution = 1)
        self.scale_E.configure(variable = self.val_E)
        self.scale_E.grid(column = 1, row = 4, padx = 10, pady = 10)

        # ----------------------------------------
        # Scale 6. : Joint 6
        # ----------------------------------------

        self.lbl_F = tk.Label(self.frame_button, text = 'Joint 6', font = self.font_lbl_middle)
        self.lbl_F.grid(column = 0, row = 5, padx = 10, pady = 10)

        self.val_F = tk.DoubleVar()
        self.scale_F = tk.Scale(self.frame_button)
        self.scale_F.configure(orient = 'horizontal', font = self.font_lbl_small, length = scale_length,
                               command = self._calc_angle)
        self.scale_F.configure(from_ = -160, to = 160, resolution = 1)
        self.scale_F.configure(variable = self.val_F)
        self.scale_F.grid(column = 1, row = 5, padx = 10, pady = 10)

        # ----------------------------------------
        # Random
        # ----------------------------------------

        self.lbl_G = tk.Label(self.frame_button, text = 'Random', font = self.font_lbl_middle)
        self.lbl_G.grid(column = 0, row = 7, padx = 10, pady = 10)

        self.btn_Random = tk.Button(self.frame_button, text='Random')
        self.btn_Random.configure(font = self.font_btn_small, width=10, command= self._calc_Random_angle)
        self.btn_Random.grid(column=1, row=7, padx=10, pady=10)

        # ----------------------------------------
        # Home
        # ----------------------------------------

        self.lbl_H = tk.Label(self.frame_button, text = 'Home', font = self.font_lbl_middle)
        self.lbl_H.grid(column = 0, row = 8, padx = 10, pady = 10)

        self.btn_Home = tk.Button(self.frame_button, text = 'Home')
        self.btn_Home.configure(font = self.font_btn_small, width = 10, command = self._calc_angle_home)
        self.btn_Home.grid(column = 1, row = 8, padx = 10, pady = 10)

        # ----------------------------------------
        # Forward Move
        # ----------------------------------------

        self.lbl_H = tk.Label(self.frame_button, text = 'Move', font = self.font_lbl_middle)
        self.lbl_H.grid(column = 0, row = 9, padx = 10, pady = 10)

        self.btn_Move = tk.Button(self.frame_button, text = 'Execute')
        self.btn_Move.configure(font = self.font_btn_small, width=10, command = self._move_myCobot)
        self.btn_Move.grid(column = 1, row = 9, padx = 10, pady = 10)




#--------------------------------------------------------
#   Program Code
#--------------------------------------------------------

    def _set_var(self):
        self.val_A.set(0.0)
        self.val_B.set(0.0)
        self.val_C.set(0.0)
        self.val_D.set(0.0)
        self.val_E.set(0.0)
        self.val_F.set(0.0)

        self.val_SS.set(50)
        self.scale_SS.set(self.val_SS.get())


    def _calc_angle(self, event=None):
        self.rad1 = self.val_A.get() * np.pi / 180
        self.rad2 = self.val_B.get() * np.pi / 180
        self.rad3 = self.val_C.get() * np.pi / 180
        self.rad4 = self.val_D.get() * np.pi / 180
        self.rad5 = self.val_E.get() * np.pi / 180
        self.rad6 = self.val_F.get() * np.pi / 180

        angles = np.array([self.rad1, self.rad2, self.rad3, self.rad4, self.rad5, self.rad6, 0])
        pos, R, self.pos_list, R_list = calc_fk(angles, JOINT_VECTORS, LINK_LENGTHS)
        self._draw_link_position(pos_list=self.pos_list)
        print('pos', pos)
        print('R', R)
        # print(pos)

    def _calc_Random_angle(self, event=None):
        self.rad1 = np.random.randint(-150,150) * np.pi/180
        self.scale_A.set(self.rad1*180/np.pi)
        self.rad2 = np.random.randint(-130, 130) * np.pi / 180
        self.scale_B.set(self.rad2 * 180 / np.pi)
        self.rad3 = np.random.randint(-130, 130) * np.pi / 180
        self.scale_C.set(self.rad3 * 180 / np.pi)
        self.rad4 = np.random.randint(-130, 130) * np.pi / 180
        self.scale_D.set(self.rad4 * 180 / np.pi)
        self.rad5 = np.random.randint(-130, 130) * np.pi / 180
        self.scale_E.set(self.rad5 * 180 / np.pi)
        self.rad6 = np.random.randint(-130, 130) * np.pi / 180
        self.scale_F.set(self.rad6 * 180 / np.pi)

        angles = np.array([self.rad1, self.rad2, self.rad3, self.rad4, self.rad5, self.rad6, 0])
        pos, R, self.pos_list, R_list = calc_fk(angles, JOINT_VECTORS, LINK_LENGTHS)
        self._draw_link_position(pos_list=self.pos_list)
        print('pos', pos)
        print('R', R)
        # print(pos)

    def _calc_angle_home(self, event=None):
        self.rad1 =0
        self.scale_A.set(0)
        self.rad2 = 0
        self.scale_B.set(0)
        self.rad3 = 0
        self.scale_C.set(0)
        self.rad4 = 0
        self.scale_D.set(0)
        self.rad5 = 0
        self.scale_E.set(0)
        self.rad6 = 0
        self.scale_F.set(0)

        angles = np.array([self.rad1, self.rad2, self.rad3, self.rad4, self.rad5, self.rad6, 0])
        pos, R, self.pos_list, R_list = calc_fk(angles, JOINT_VECTORS, LINK_LENGTHS)
        self._draw_link_position(pos_list=self.pos_list)
        print('pos', pos)
        print('R', R)
        # print(pos)

    def _draw_link_position(self, pos_list, dof=6):
        iter_num = dof + 1
        ax.cla()
        # ax.set_title("myCobotSim", size = 20)
        ax.set_xlabel("x", size = 10, color = "black")
        ax.set_ylabel("y", size = 10, color = "black")
        ax.set_zlabel("z", size = 10, color = "black")
        ax.set_xlim3d(-0.3, 0.3)
        ax.set_ylim3d(-0.2, 0.2)
        ax.set_zlim3d(0, 0.4)
        for i in range(iter_num):
            if i == 0:
                axs = ax.plot([pos_list[i, 0], pos_list[i + 1, 0]],
                              [pos_list[i, 1], pos_list[i + 1, 1]],
                              [pos_list[i, 2], pos_list[i + 1, 2]],
                              color = 'gray',
                              linewidth = 10)
            else:
                axs += ax.plot([pos_list[i, 0], pos_list[i + 1, 0]],
                               [pos_list[i, 1], pos_list[i + 1, 1]],
                               [pos_list[i, 2], pos_list[i + 1, 2]],
                               color = 'blue')
        ax.scatter(pos_list[:, 0], pos_list[:, 1], pos_list[:, 2], color = 'red')

        self.canvas.draw()

    def _move_myCobot(self):
        list_angle_rad = [self.rad1,self.rad2,self.rad3,self.rad4,self.rad5,self.rad6]
        speed = self.val_SS.get()
        mycobot.send_radians(list_angle_rad, speed)

    def _stop_myCobot(self):
        mycobot.pause()

    def _release_myCobot(self):
        mycobot.set_free_mode()

    def _flash_LED(self):
        global state_LED
        r = lambda: random.randint(0, 255)
        color = '%02X%02X%02X' % (r(),r(),r())
        print(color)

        if state_LED == True:
            state_LED = False
            mycobot.set_led_color('000000')
            self.btn_LED.configure(text='LED OFF')
        else:
            state_LED = True
            mycobot.set_led_color(color)
            self.btn_LED.configure(text = 'LED ON')






#--------------------------------------------------------
#   Outscope of Tkinter Class
#--------------------------------------------------------

fig = Figure(figsize = (6.5,5.52), dpi=100)
ax = fig.add_subplot(111,projection='3d')




def main():
    root = tk.Tk()
    app = Application(master=root)  #Inherit
    app.mainloop()

if __name__ == "__main__":
    main()