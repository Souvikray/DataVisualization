from matplotlib import pyplot as plt
import numpy as np


# define the x axis
x = np.linspace(0, 10)
# create the first subplot
velocity_plot = plt.subplot(2, 1, 1)  # (row, col, id)
# everything from now will be defined for subplot 1 unless another subplot defined
plt.plot(x, np.sin(x), "-", label="sin")  # (x, y -> it will take y points from the sin function, plot_type, label)
# add a label to the y axis
plt.ylabel("Velocity (m/s)")
# hide the x axis
plt.setp(velocity_plot.get_xticklabels(), visible=False)
# allow grid
plt.grid(True)

# create the second subplot
plt.subplot(2, 1, 2, sharex=velocity_plot)  # get the x axis from the velocity_plot
plt.plot(x, np.cos(x), "-", label="cos")
plt.ylabel("Acceleration (m/s/s)")
plt.grid(True)
# display the legend
plt.legend()
# show the plot
plt.show()


