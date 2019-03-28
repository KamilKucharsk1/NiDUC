
import matplotlib.pyplot as plt

def hist(m):

    n, bins, patches = plt.hist(m, 25, density=True, facecolor='g', alpha=0.75)
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.axis([0, 256, 0, 0.03])
    plt.grid(True)
    plt.show()