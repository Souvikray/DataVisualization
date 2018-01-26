from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# meshgrid creates a rectangular grid out of an array of x values and an array of y values.
x, y = np.meshgrid(np.arange(-100, 100), np.arange(-100, 100))  # (x, y) will have every possible coordinates
# define the z axis
z = x ** 2 + y ** 2  # for every value of x and y, z will be square of them added up
# get a figure object
fig = plt.figure()
# get a 3D axes object (x, y, z)
axes = fig.gca(projection='3d')
# plot the 3D axes
axes.plot_surface(x, y, z)
# show the plot
plt.show()

