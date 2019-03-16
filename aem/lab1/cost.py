import numpy as np

from .mst import MST

def clustering_cost(distances, clusters):
    cost = 0.0
    for cluster in clusters:
        mst = MST(distances, cluster)
        mst.find()
        cost += mst.cost
    return cost
