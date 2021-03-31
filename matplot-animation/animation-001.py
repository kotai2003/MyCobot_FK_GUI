#https://qiita.com/yubais/items/c95ba9ff1b23dd33fde2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()


ims = []
n_pics = 10

for i in range(n_pics):
    rand = np.random.randn(100)
    im = plt.plot(rand)
    ims.append(im)


# interval 100ms
ani = animation.ArtistAnimation(fig, ims, interval = 100)
# plt.show()

ani.save('output.gif', writer='imagemagick')

