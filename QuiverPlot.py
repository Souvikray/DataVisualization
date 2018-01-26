from matplotlib import pyplot as plt
import numpy as np


# meshgrid creates a rectangular grid out of an array of x values and an array of y values.
x, y = np.meshgrid(np.arange(-10, 10), np.arange(-10, 10))  # (x, y) will have every possible coordinates
u = -y  # moves x by u
v = x  # moves y by v
# plot the quiver plot
plt.quiver(x, y, u, v)
# plot the stream plot
# plt.streamplot(x, y, u, v)
# show the plot
plt.show()
