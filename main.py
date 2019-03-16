#!/usr/bin/env python3

import math
import itertools

def load_points(filename):
    points = []
    with open(filename) as f:
        for line in f:
            x, y = line.split(' ')[0:2]
            point = (int(x), int(y))
            points.append(point)
    return points

def distances(points):
    matrix = {}
    for a, b in itertools.product(points, points):
        (x1, y1) = a
        (x2, y2) = b
        matrix[a, b] = math.hypot(x1 - x2, y1 - y2)
    return matrix

def minimum_spanning_tree(points):
    pass

points = load_points('data.txt')

