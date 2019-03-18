import unittest

import numpy as np

from aem.lab1.cluster import cluster, forest_to_labels
from aem.lab1.data_import import distance_matrix

class ClusterTest(unittest.TestCase):
    def __init__(self, *args):
        super(ClusterTest, self).__init__(*args)
        self.distances = distance_matrix(np.array([
            [1, 1],
            [3, 4],
            [3, 1],
            [4, 2],
            [6, 3],
            [7, 1]
        ]))

    def test_forest_to_labels(self):
        forest = {(0, 2), (1, 3), (2, 3), (4, 5)}
        labels = forest_to_labels(forest, 6, 2)
        print(labels)
        assert(labels[0] == labels[1] == labels[2] == labels[3])
        assert(labels[4] == labels[5])
        assert(labels[0] != labels[4])
