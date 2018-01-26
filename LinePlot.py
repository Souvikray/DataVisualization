from matplotlib import pyplot as plt
import numpy as np


# define the x axis for both the waves
x = np.linspace(0, 10)  # returns an evenly spaced number over a specified interval
# define the y axis for sin wave
y1 = np.sin(x)
# define the y axis for cos wave
y2 = np.cos(x)
# plot the sin wave
plt.plot(x, y1, 'g-', label="sin")
# plot the cos wave
plt.plot(x, y2, 'b-', label="cos")
# display the legend
plt.legend()
# show the plot
plt.show()
