from matplotlib import pyplot as plt


# define the labels for the pie chart
labels = ["rent", "grocery", "shopping", "eatout", "savings"]
# assign value to each of the items
values = [4000, 600, 1500, 1600, 2300]
# cut out the desired pie
explode = [0, 0, 0, 0, 1]  # 0 -> False, 1 -> True
# plot the pie chart
plt.pie(values, labels=labels, explode=explode, radius=0.75, shadow=True, autopct='%.2f')
# show the plot
plt.show()
