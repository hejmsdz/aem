import matplotlib.pyplot as plt
import numpy as np
import pylab

from .mst import MST

def plot_solution(points, distances, labels):
    x, y = points.T
    colors = [f"C{i}" for i in labels]
    plt.scatter(x, y, c=colors)

    clusters = [set() for _ in range(max(labels) + 1)]
    for (i, label) in enumerate(labels):
        clusters[label].add(i)

    lines = []
    for i, cluster in enumerate(clusters):
        mst = MST(distances, cluster)
        mst.find()
        for (a, b) in mst.tree:
            x1, y1 = points[a]
            x2, y2 = points[b]
            lines.extend([(x1, x2), (y1, y2), f"C{i}"])

    plt.plot(*lines)

    pylab.show()
