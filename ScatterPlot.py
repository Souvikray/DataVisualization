from matplotlib import pyplot as plt


# define the x coordinates of the points
x = [17, 34, 54, 23, 67, 45, 10]
# define the y coordinates of the points
y = [45, 55, 24, 67, 60, 35, 73]
# plot the coordinates
plt.scatter(x, y, s=60, c='r', marker='*')  # (x, y, size_of_marker, color, marker_symbol)
# show the plot
plt.show()
