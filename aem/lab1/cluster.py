import collections

import numpy as np

from .mst import MST

def cluster(distances, n_clusters):
    mst = MST(distances)
    mst.find()
    tree = np.array([[*edge, distances[edge]] for edge in mst.tree])
    num_edges_to_remove = n_clusters - 1
    edge_indices = np.argpartition(tree[:, 2], -num_edges_to_remove)[-num_edges_to_remove:]
    longest_edges = tree[edge_indices, :]
    forest = mst.tree.copy()
    for (a, b, _cost) in longest_edges:
        forest.remove((a, b))
    
    return forest_to_labels(forest, distances.shape[0], n_clusters)

def forest_to_labels(forest, n, n_clusters):
    labels = np.full(n, -1, dtype=int)
    clusters = collections.defaultdict(set)
    next_label = 0
    for (a, b) in forest:
        added = False
        for (i, cluster) in enumerate(clusters):
            if a in cluster or b in cluster:
                labels[a] = i
                labels[b] = i
                cluster.add(a)
                cluster.add(b)
                added = True
                break
        if not added:
            labels[a] = next_label
            labels[b] = next_label
            clusters[next_label].add(a)
            clusters[next_label].add(b)
            next_label += 1

    return labels
