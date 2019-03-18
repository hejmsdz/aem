import numpy as np

from itertools import islice

def clusters_to_labels(n, clusters):
    labels = np.full(n, -1, dtype=int)
    for j, cluster in enumerate(clusters):
        for i in cluster:
            labels[i] = j

    return labels

def insert_to_nearest(point, clusters, distances):
    nearest = min(clusters, key=lambda cluster: distances[point, cluster].min())
    nearest.append(point)
    return nearest
