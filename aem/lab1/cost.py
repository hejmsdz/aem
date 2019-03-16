import numpy as np

from .mst import MST

def clustering_cost(distances, clusters):
    print('testing')
    cost = 0
    for cluster in clusters:
        mst = MST(distances, cluster)
        mst.find()
        print(mst.tree)
        cost += mst.cost
    return cost
