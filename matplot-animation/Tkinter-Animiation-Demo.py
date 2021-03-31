import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation



class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.master.geometry("800x600")
        self.master.title("Tkinter Animation")
        self.master.resizable(True, True)

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
        self.logo_img = Image.open('./image/Logo_Small_new.png')
        self.logo_img = self.logo_img.resize((182, 57))
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.cav_logo = tk.Canvas(self.frame_logo, width = 182, height = 57)
        self.cav_logo.create_image(5, 5, image = self.logo_img, anchor = 'nw')
        self.cav_logo.grid(column = 0, row = 0, padx = 10, pady = 10)

        # ----------------------------------------
        # Canvas_Frame
        # ----------------------------------------
        canvas_width = 560
        canvas_height = 460

        self.frame_canvas = ttk.Frame(self.tab1)
        self.frame_canvas.configure(width = canvas_width, height = canvas_height)
        self.frame_canvas.place(relx = 0.01, rely = 0.15)
        self.frame_canvas.grid_propagate(0)

        # self.canvas1 = tk.Canvas(self.tab1)
        # self.canvas1.configure(width = canvas_width, height = canvas_height)
        # self.canvas1.create_rectangle(0,0,canvas_width,canvas_height, fill='white')
        # self.canvas1.place(relx=0.01, rely=0.15)


        #########################################
        # Frame : Buttons
        #########################################
        self.frame_buttons = ttk.Frame(self.tab1)
        self.frame_buttons.configure(width = 200, height = 300)
        self.frame_buttons.place(relx=0.75, rely=0.15)
        self.frame_buttons.grid_propagate(0)

        # ----------------------------------------
        #  Button 1. Start
        # ----------------------------------------
        self.btn_start = tk.Button(self.frame_buttons, text='Start', font = self.font_btn_small)
        self.btn_start.configure(command = self._start_ani, width = 10)
        self.btn_start.grid(column = 0, row=0, padx= 10, pady=10, sticky='we')

        # ----------------------------------------
        #  Button 2. Stop
        # ----------------------------------------
        self.btn_stop = tk.Button(self.frame_buttons, text = 'Stop', font = self.font_btn_small)
        self.btn_stop.configure(command = self._stop_ani)
        self.btn_stop.grid(column = 0, row = 1, padx = 10, pady = 10, sticky = 'we')

        # ----------------------------------------
        #  Button 3. Quit
        # ----------------------------------------
        self.btn_quit = tk.Button(self.frame_buttons, text = 'Quit', font = self.font_btn_small)
        self.btn_quit.configure(command = self._quit)
        self.btn_quit.grid(column = 0, row = 2, padx = 10, pady = 10, sticky = 'we')


#--------------------------------------------------------
#   Program Code
#--------------------------------------------------------

    def _start_ani(self):

        fig = plt.figure(figsize=(3,2.5), dpi=100)


        self.canvas2 = FigureCanvasTkAgg(fig, master=self.frame_canvas)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(side= tk.TOP, fill=tk.BOTH, expand=True)
        self.ax = fig.add_subplot(1,1,1)

        self.ani = animation.FuncAnimation(fig, func = self._plot_data, interval = 100)



    def _stop_ani(self):
        pass

    def _quit(self):
        pass

    def _plot_data(self, event):

        rand = np.random.randn(100)     #100個の乱数を生成
        self.ax.clear()
        self.ax.plot(rand)
        #グラフを生成





    def _draw_Ani(self):
        pass



def main():
    root = tk.Tk()
    app = Application(master=root)  #Inherit
    app.mainloop()

if __name__ == "__main__":
    main()