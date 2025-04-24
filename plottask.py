# weekly task 8
# plot a histogram of a normal distribution of a 1000 values with a mean of 5 and deviation of 2
# and a plot of the function h(x)=x^3 in the range 0 to 10
# author: Dave Byrne :)

import numpy as np
import matplotlib.pyplot as plt

# generate 1000 values from a normal distribution
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# create x values for function
x = np.linspace(0, 10, 100)
h = x ** 3

# create plot
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, alpha=0.5, color='blue', label='Normal Distribution')
plt.plot(x, h, color='red', label='h(x)=x^3')
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()

# show plot
plt.show()

'''
I ran into an issue with VSCode and Python while coding this.
It failed to find PyLance and kind of crashed Python altogether on me.
Now that I'm using a codespace, I'm using chatgpt for the final portion
of this code to show me how to load a png file and verify that my code is
working on this codespace.
'''

plt.savefig('plot.png')

print("Plot saved as 'plot.png'.")