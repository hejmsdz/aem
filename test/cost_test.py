import unittest

import numpy as np

from aem.lab1.cost import clustering_cost
from aem.lab1.data_import import distance_matrix

class CostTest(unittest.TestCase):
    def __init__(self, *args):
        super(CostTest, self).__init__(*args)
        self.distances = distance_matrix(np.array([
            [1, 1],
            [3, 4],
            [3, 1],
            [4, 2],
            [6, 3],
            [7, 1]
        ]))

    def test_cost(self):
        examples = [
            ([{0, 1, 2}, {3, 4, 5}], 9.47213595499958),
            ([{1, 4, 5}, {0, 2, 3}], 8.812559200041264),
            ([{1, 3}, {0, 2, 4, 5}], 10.07768723046357),
            ([{0}, {1}, {2}, {3}, {4}, {5}], 0.0)
        ]
        for (clusters, expected_cost) in examples:
            cost = clustering_cost(self.distances, clusters)
            self.assertAlmostEqual(cost, expected_cost)
