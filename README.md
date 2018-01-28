**Data visualization** is a general term that describes any effort to help people understand the significance of data by placing it in a visual context. Patterns, trends and correlations that might go undetected in text-based data can be exposed and recognized easier with data visualization.

With interactive visualization, we can take the concept a step further by using technology to drill down into charts and graphs for more detail, interactively changing what data we see and how it’s processed.
 
Python provides a module to plot and visualize data called ```matplotlib```.Together with ```numpy``` module, you can perform analysis, calculate numbers and represent data as models. 

Let us go through each of the models one by one

**Note: I have taken random values to create graphs or plot data below.**

## Bar Chart

A bar chart represents categorical data with rectangular bars with heights or lengths proportional to the values that they represent. The bars can be plotted vertically or horizontally.Below is a bar chart that shows the performance of students when put under Prof B and Prof G. Clearly Prof B is a better teacher.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot1.png?raw=true "Optional Title")

## Sub Plots

When we represent two or more plots that share the same x or y axis, they are called sub plots.Below we have two graph representations ```sin``` and ```cos``` that share the same x axis.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot2.png?raw=true "Optional Title")

## Histogram

A histogram is a graphical display of data using bars of different heights. In a histogram, each bar groups numbers into ranges. Taller bars show that more data falls in that range.They more or less follow the **normal distribution.**

**Normal Distribution**

There are cases where the data tends to be around a central value with no bias left or right, and it gets close to what is called 'Normal Distribution' like below.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot3:2.jpg?raw=true "Optional Title")

Many things closely follow a Normal Distribution such as heights of people, blood pressure etc. Below is a histogram that follows Normal Distribution.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot3.png?raw=true "Optional Title")

## Pie Chart

A pie chart is a circular statistical graph which is divided into slices to illustrate numerical proportion. In a pie chart, the arc length of each slice, is proportional to the quantity it represents. Below is a pie chart that represents my monthly expenses and how much I am able to save every month.Clearly I am able to save only 23% of my pocket money.Gotta start saving more!

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot4.png?raw=true "Optional Title")

## Box Plot

A box plot is a standardized way of displaying the distribution of data based on the five number summary.

**Five number Summary**

Five number summary consists of the following parameters: minimum, first quartile, median, third quartile, and maximum. Any data can be represented by a Five number summary that gives an overall view of the data.

Below is a box plot that gives information about the five parameters.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot5.png?raw=true "Optional Title")

Clearly looking at it, we can derive the following information

min: 0.93

Q1: (0.9 - 16.9)

median: 17.24

Q3: (68.91 - 98.04)

max: 98.04

## Line Plot

A line plot is a graph that shows the frequency of data occuring along a number line.Below is a line plot where the sin(x) and cos(x) finctions are plotted on the number line.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot6.png?raw=true "Optional Title")

## Scatter Plot

A Scatter (XY) Plot has points that show the relationship between two sets of data.Below is a scatter plot that shows the relationship (X, Y) for the two sets of data X and Y.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot7.png?raw=true "Optional Title")

## Quiver Plot

A quiver plot displays velocity vector as arrows with components (u, v) at the points (x, y).

x, y: The coordinate for the point
u, v: The displacement for eg **x** has moved by **u** and **y** has moved by **v**

quiver(x, y, u, v) plots vectors as arrows at the coordinates specified in each pair of elements in **x** and **y**

Below is a quiver plot for x and y axis each of (-10, 10).

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot8.png?raw=true "Optional Title")

It can be used for example to plot ocean currents.

## 3D Line Plot

It displays a three-dimensional plot of a set of data points.Below is a quiver plot that generates a 3D plot for given points along X, Y and Z axis.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot9.png?raw=true "Optional Title")

## 3D Surface Plot

It is a three-dimensional surface plot that plots the values in matrix Z as heights above a grid in the x-y plane defined by X and Y.

Below is a 3D surface plot that generates a surface for given points along X, Y and Z axis.Here z is a function of x and y where for each value of x and y, z is the sum of square of x and y.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot10.png?raw=true "Optional Title")

Now let us do some real world analysis of data.I have implemented a scatter plot to display word frequency for a given word in a book.

The book is titled 'The Art of Public Speaking' by Dale Carnegie (it is an amazing book by the way!) available for free from the website [www.gutenberg.org](http://www.gutenberg.org).You can use the Linux commad below to download the content of the book and save it to a .txt file.

```curl http://www.gutenberg.org/cache/epub/16317/pg16317.txt --output public-speaking.txt```

Let us look for the occurence of a word **confidence** in the book.Below is a scatter plot for the result obtained.

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot11.png?raw=true "Optional Title")

Clearly we can see that the word 'confidence' has a rank of **576** and has occured around **50** times.

Let us do it once again for another word.Let us look for the occurence of a word **public**

![Alt text](https://github.com/Souvikray/DataVisualization/blob/master/screenshot12.png?raw=true "Optional Title")

Once again we can see that the word 'public' has a rank of **110** and has occured around **100** times.












 
 
