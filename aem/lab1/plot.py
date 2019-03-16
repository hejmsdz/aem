import matplotlib.pyplot as plt
import pylab

def plot_solution(points, clusters):
    x, y = points.T
    plt.scatter(x, y)
    pylab.show()
