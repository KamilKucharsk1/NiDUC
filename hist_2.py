import numpy as np
import matplotlib.pyplot as plt
x=[3,55,77,88,109]

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()