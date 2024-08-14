# Taylor series is an important mathematical concept that helps to approximate functions using polynomials

# Here, write a function that uses taylor series to approximate the function f(x) = sin(x) over the domain -2pi to 2pi

# Use numpy and matplotlib to plot your results and display them in the colour blue

# plot the real value of f(x) = sin(x) on the same plot in the colour red

import matplotlib.pyplot as plt
import numpy as np
import math as math

def Taylor_Series(x):
    """
    This funciton takes an input (x) with a defined taylor series function (in this case sin(x)).
    It outputs a value, y, after summing a specified range of the series (n).
    """
    sum=0
    for n in range(0,11):
        y = ((-1)**n * x**(2*n+1))/(math.factorial(2*n+1))
        sum += y
    return sum

x_range = np.arange(-2*math.pi,2*math.pi,.1) ## Makes the x range for the plot
output1 = [] ## Initial list for our taylor series function
for i in x_range:
    y = Taylor_Series(i) ##Iterates through taylor series with the defined domain
    output1.append(y)
y_range1 = np.array(output1) ##This is the y range for the taylor approximation in an array format to plot
y_range2 = np.sin(x_range) ##This is the second graph of the true sin(x) function to compare with Taylor

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5)) ##This creates space for 2 plots##

ax1.plot(y_range1, color = 'blue') ##First plot of Taylor Approximation sin(x)

ax2.plot(y_range2, color = 'red')##Second plot of true sin(x)

plt.tight_layout()##formatting function
plt.show()