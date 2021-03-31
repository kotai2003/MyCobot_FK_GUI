#https://qiita.com/yubais/items/c95ba9ff1b23dd33fde2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()


def plot(data):
    plt.cla() # clear the figure
    rand = np.random.randn(100)
    plt.plot(rand)


# interval 100ms
ani = animation.FuncAnimation(fig, plot, interval = 100)
plt.show()

# ani.save('output.gif', writer='imagemagick')

