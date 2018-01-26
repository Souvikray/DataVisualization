from matplotlib import pyplot as plt
# if just one parameter (list) is passed, it assumes it to be the points for y axis
# so it automatically creates the x axis for you of same length (0 - 3)
#plt.plot([1, 2, 3, 4])
#plt.show()

# to plot both x and y axis
plt.plot([1, 2, 3, 4], [2, 4, 9, 16], 'ro')  # ro: r- red, o- circle
# set the limits for x and y axis
plt.axis([0, 10, 0, 20])  # [xmin, xmax, ymin, ymax]
# show the plot
plt.show()
