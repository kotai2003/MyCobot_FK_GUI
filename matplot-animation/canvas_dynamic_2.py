# https://water2litter.net/rum/post/python_tkinter_matplotlib/

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Matplotlib in tkinter')
        self.pack()
        self.create_widgets()

        self.start_up()
        self.draw_plot()

    def create_widgets(self):
        self.canvas_frame = tk.Frame(self.master)
        self.canvas_frame.pack(side=tk.LEFT)
        self.control_frame = tk.Frame(self.master)
        self.control_frame.pack(side=tk.RIGHT)

        self.canvas = FigureCanvasTkAgg(fig, self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.canvas_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.x_v = tk.DoubleVar()
        self.x_scale = tk.Scale(self.control_frame,
            variable=self.x_v,
            from_=0.0,
            to=10.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            command=self.draw_plot)
        self.x_scale.pack(anchor=tk.NW)

        self.y_v = tk.DoubleVar()
        self.y_scale = tk.Scale(self.control_frame,
            variable=self.y_v,
            from_=0.0,
            to=10.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            command=self.draw_plot)
        self.y_scale.pack(anchor=tk.NW)

    def start_up(self):
        self.x_v.set(1.0)
        self.y_v.set(1.0)

    def draw_plot(self, event=None):
        global h
        v = self.x_v.get()
        print('v',v)
        w = self.y_v.get()
        t = np.arange(0.0, 6.29, 0.01)
        x = np.cos(v * t)
        y = np.sin(w * t)
        h.set_xdata(x)
        h.set_ydata(y)
        self.canvas.draw()

fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-1.2,1.2)
h, = ax.plot([],[], 'green')

root = tk.Tk()
app = Application(master=root)
app.mainloop()