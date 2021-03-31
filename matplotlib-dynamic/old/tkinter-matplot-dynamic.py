import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import math


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)


        self.master.geometry("1000x800")
        self.master.title("GUI Template")
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
        self._draw_plot()


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
        self.logo_img = Image.open('../../image/Logo_Small_new.png')
        self.logo_img = self.logo_img.resize((182, 57))
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.cav_logo = tk.Canvas(self.frame_logo, width = 182, height = 57)
        self.cav_logo.create_image(5, 5, image = self.logo_img, anchor = 'nw')
        self.cav_logo.grid(column = 0, row = 0, padx = 10, pady = 10)

        #########################################
        # Frame for  Canvas
        #########################################
        self.frame_canvas = tk.LabelFrame(self.tab1, text='Canvas')
        self.frame_canvas.configure(width = 650, height = 600)
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
        # Frame : Button
        #########################################
        self.frame_button = tk.LabelFrame(self.tab1, text='Button')
        self.frame_button.configure(width = 250, height = 600)
        self.frame_button.place(x = 680, y = 100)
        self.frame_button.grid_propagate(0)

        #----------------------------------------
        # Scale 1. : A
        #----------------------------------------
        scale_length = 100
        self.lbl_A = tk.Label(self.frame_button, text = 'Amplitute', font = self.font_lbl_middle)
        self.lbl_A.grid(column = 0, row = 0, padx = 10, pady = 10)

        self.val_A = tk.DoubleVar()
        self.scale_A = tk.Scale(self.frame_button)
        self.scale_A.configure(orient = 'horizontal', font = self.font_lbl_small, length = scale_length,command=self._draw_plot)
        self.scale_A.configure(from_ = 1, to = 10, resolution = 0.1)
        self.scale_A.configure(variable = self.val_A)
        self.scale_A.grid(column = 1, row = 0, padx = 10, pady = 10)

        #----------------------------------------
        # Scale 1. : B
        #----------------------------------------
        scale_length = 100
        self.lbl_B = tk.Label(self.frame_button, text = 'Phase', font = self.font_lbl_middle)
        self.lbl_B.grid(column = 0, row = 1, padx = 10, pady = 10)

        self.val_B = tk.DoubleVar()
        self.scale_B = tk.Scale(self.frame_button)
        self.scale_B.configure(orient = 'horizontal', font = self.font_lbl_small, length = scale_length,command=self._draw_plot)
        self.scale_B.configure(from_ = 1, to = 10, resolution = 0.1)
        self.scale_B.configure(variable = self.val_B)
        self.scale_B.grid(column = 1, row = 1, padx = 10, pady = 10)


#--------------------------------------------------------
#   Program Code
#--------------------------------------------------------

    def _set_var(self):
        self.val_A.set(1.0)
        self.val_B.set(2.0)


    def _draw_plot(self, event=None):

        global h
        Amp = self.val_A.get()
        print(Amp)
        Phs = self.val_B.get()
        t = np.arange(0.0, 2*math.pi, 0.01*math.pi)
        y = Amp * np.cos(Phs * t)
        h.set_xdata(t)
        h.set_ydata(y)
        self.canvas.draw()

#--------------------------------------------------------
#   Outscope of Tkinter Class
#--------------------------------------------------------

fig = Figure(figsize = (6.5,5.4), dpi=100)
ax = fig.add_subplot(111)
ax.set_xlim(0, 2*math.pi)
ax.set_ylim(-5,5)
h, = ax.plot([],[], 'green')


def main():
    root = tk.Tk()
    app = Application(master=root)  #Inherit
    app.mainloop()

if __name__ == "__main__":
    main()