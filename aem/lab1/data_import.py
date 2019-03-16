import itertools

import numpy as np

def load_points(filename):
    points = []
    with open(filename) as f:
        for line in f:
            point = [int(val) for val in line.split(' ')[0:2]]
            points.append(point)
    return np.array(points)

def distance_matrix(points):
    n = points.shape[0]
    matrix = np.zeros((n, n))

    for i, j in itertools.product(range(n), repeat=2):
        matrix[i, j] = np.linalg.norm(points[i] - points[j])
    
    return matrix
