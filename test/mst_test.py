import unittest

import numpy as np

from aem.lab1.mst import MST
from aem.lab1.data_import import distance_matrix

class MSTTest(unittest.TestCase):
    def __init__(self, *args):
        super(MSTTest, self).__init__(*args)
        self.distances = distance_matrix(np.array([
            [1, 1],
            [3, 4],
            [3, 1],
            [4, 2],
            [6, 3],
            [7, 1]
        ]))
        self.mst = MST(self.distances)
        self.mst.find()

    def test_tree(self):
        expected_tree = {(0, 2), (1, 3), (2, 3), (3, 4), (4, 5)}
        self.assertEqual(self.mst.tree, expected_tree)

    def test_cost(self):
        expected_cost = 10.122417494872465
        self.assertAlmostEqual(self.mst.cost, expected_cost)

