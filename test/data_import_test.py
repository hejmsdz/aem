import os.path
import unittest

import numpy as np

from aem.lab1.data_import import load_points, distance_matrix

class DataImportTest(unittest.TestCase):
    def test_load_points(self):
        filename = os.path.join(os.path.dirname(__file__), '../data/three.txt')
        points = load_points(filename)
        expected_points = np.array([[0, 0], [4, 0], [0, 3]])
        np.testing.assert_equal(points, expected_points)

    def test_distance_matrix(self):
        points = np.array([[0, 0], [4, 0], [0, 3]])
        matrix = distance_matrix(points)
        expected_matrix = np.array([[0, 4, 3], [4, 0, 5], [3, 5, 0]])
        np.testing.assert_equal(matrix, expected_matrix)
