import random

import numpy as np

from .utils import insert_to_nearest, clusters_to_labels

def cluster(distances, n_clusters):
    n = distances.shape[0]
    points = list(range(n))
    random.shuffle(points)
    clusters = [list() for _ in range(n_clusters)]

    for cluster, i in zip(clusters, points):
        cluster.append(i)
    
    for i in points[n_clusters:]:
        insert_to_nearest(i, clusters, distances)
    
    return clusters_to_labels(n, clusters)
