import matplotlib.pyplot as plt
import numpy as np


# number of ticks on x axis
num_bins = 5
# set the bar width
bar_width = 0.25
# property for first set of bars
# here there will be 5 bars representing 5 students who will get random marks between 0 to 100
bar1 = np.random.randint(0, 100, num_bins)
# set up second set of bars
bar2 = np.random.randint(0, 100, num_bins)
# arrange the bars
indices = np.arange(num_bins)
# plot the bars
plt.bar(indices, bar1, bar_width, color='b', label="Prof B")
plt.bar(indices + bar_width, bar2, bar_width, color='g', label="Prof G")
# label the points on X axis
plt.xticks(indices + (bar_width / 2), ('A', 'B', 'C', 'D', 'F'))
# display the x axis label
plt.xlabel("Grade")
# display the y axis label
plt.ylabel("Marks")
# display the legend
plt.legend()
# show the plot
plt.show()
