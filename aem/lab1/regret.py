import random
from itertools import permutations

import numpy as np

from .utils import insert_to_nearest, clusters_to_labels

def cluster(distances, n_clusters):
    n = distances.shape[0]
    points = list(range(n))
    random.shuffle(points)
    clusters = [list() for _ in range(n_clusters)]

    for cluster, i in zip(clusters, points):
        cluster.append(i)
    
    for i in range(n_clusters, n - 1):
        a = points[i]
        b = points[i + 1]
        ab_cost = sequence_cost([a, b], clusters, distances)
        ba_cost = sequence_cost([b, a], clusters, distances)

        if ab_cost > ba_cost:
            points[i + 1] = a
            a = b

        insert_to_nearest(a, clusters, distances)

        if i == n - 2:
            insert_to_nearest(b, clusters, distances)
    
    return clusters_to_labels(n, clusters)

def sequence_cost(sequence, existing_clusters, distances):
    clusters = [cluster[:] for cluster in existing_clusters]
    cost = 0.0
    for i in sequence:
        nearest = insert_to_nearest(i, clusters, distances)
        cost += distances[i, nearest].min()
    return cost
