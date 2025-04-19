# weekly task 8
# plot a histogram of a normal distribution of a 1000 values with a mean of 5 and deviation of 2
# and a plot of the function h(x)=x^3 in the range 0 to 10
# author: Dave Byrne :)

import numpy as np
import matplotlib.plyplot as plt

# create plot
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, alpha=0.5, colour='blue', label='Normal Distribution')
plt.plot(x, y, colour='red', label='h(x)=x^3')
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('Frequency')
plt.(legend())
plt.grid(True)
plt.tight_layout()

