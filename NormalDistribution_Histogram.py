from matplotlib import pyplot as plt
import numpy as np


# define a mean for the normal distribution
mu = 0
# define by how much the data should be spread out (also called standard deviation)
sigma = 10  # in this case by a factor of 10
# calculate appropriate values that has the given mu and sigma and satisfies the condition for normal distribution
values = mu + sigma * np.random.randn(1000)
# plot the histogram
plt.hist(values, 50, ec='black')  # (values, no_of_bins, edge_color)
# add a label to the x axis
plt.xlabel("bins")
# add a label to the y axis
plt.ylabel("frequency")
# add a title to the plot
plt.title("Normal Distribution")
# show the plot....in this case a histogram
plt.show()

