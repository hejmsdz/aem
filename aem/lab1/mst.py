import numpy as np

import itertools

class MST:
    def __init__(self, distances, vertices=None):
        self.distances = distances
        
        if vertices is None:
            vertices = range(distances.shape[0])
        self.vertices = {i: (float('inf'), None) for i in vertices}

        self.tree = set()
        self.cost = 0.0
    
    def next_vertex(self):
        vertex = min(self.vertices, key=lambda i: self.vertices[i][0])
        _cost, neighbour = self.vertices.pop(vertex)
        return vertex, neighbour

    def find(self):
        while self.vertices:
            vertex, neighbour = self.next_vertex()
            self.include(vertex, neighbour)
        return self.tree, self.cost
    
    def include(self, vertex, neighbour):
        if neighbour is not None:
            self.tree.add(self.pair(vertex, neighbour))
            self.cost += self.distances[vertex, neighbour]
        for (other, (cost, _)) in self.vertices.items():
            if self.distances[vertex, other] < cost:
                self.vertices[other] = (self.distances[vertex, other], vertex)

    def pair(self, a, b):
        return (a, b) if a <= b else (b, a)
