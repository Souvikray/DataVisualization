from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# define an axis
phi = np.linspace(-6 * np.pi, 6 * np.pi, 100)
# define the z axis
z = np.linspace(-4, 4, 100)
# define the x axis
x = np.sin(phi)
# define the y axis
y = np.cos(phi)
# get a figure object
fig = plt.figure()
# get a 3D axes object (x, y, z)
axes = fig.gca(projection='3d')
# plot the 3D axis
axes.plot(x, y, z)
# show the plot
plt.show()
