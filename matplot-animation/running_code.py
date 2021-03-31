import tkinter as tk
import numpy as np
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation, figure
# https://www.javaer101.com/ja/article/43012407.html

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        fig = figure.Figure()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(column=0, row=0)
        self.ax = fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        self.zs = []

        self.ani = animation.FuncAnimation(fig, self.animate, interval=5)

    def animate(self, event):
        self.xs.append(time.clock())
        self.ys.append(time.clock() + np.random.random())
        self.xs = self.xs[-100:]
        self.ys = self.ys[-100:]
        self.ax.clear()
        self.ax.plot(self.xs, self.ys)


if __name__ == "__main__":
    App().mainloop()