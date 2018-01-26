from matplotlib import pyplot as plt
import numpy as np


# get 100 floating points whose value is between 0 and 100
x = np.random.rand(100) * 100  # the x axis will be defined based on the value of the 100 points
# plot the horizontal boxplot
plt.boxplot(x, vert=False)
# show the plot
plt.show()
