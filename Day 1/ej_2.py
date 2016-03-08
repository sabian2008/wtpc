"""
Load the data and fit a third degree polynomial
"""

# Load libs
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Load data
x = [7.5, 4.48, 8.60, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06]
y = [28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68, 21.89] 

# Transform into numpy arrays
x = np.asarray(x)
y = np.asarray(y)

# Get fit data
fit_coef= np.polyfit(x, y, 3)
poly = np.poly1d(fit_coef) # Turns coeficients into a polynomial function


# Graph domain
xi = np.linspace(math.floor(min(x)),math.ceil(max(x)),100)


# Print data
plt.scatter(x,y)
plt.plot(xi,poly(xi),'r-')
plt.grid(True)
plt.show()
