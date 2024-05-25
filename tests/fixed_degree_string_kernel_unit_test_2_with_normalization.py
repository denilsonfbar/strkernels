
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import time
import numpy as np
import math

# kernel class import
from sys import path
path.append('..')
from strkernels import FixedDegreeStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.kernel = FixedDegreeStringKernel(degree=1)

    def test_single_set(self):
        strings = np.array(["ATCG", "ATGG", "TACG", "GCTA"])
        expected_matrix = np.array([
            [4, 3, 2, 0],
            [3, 4, 1, 0],
            [2, 1, 4, 0],
            [0, 0, 0, 4]
        ])

        denominator = expected_matrix[0, 0]
        expected_matrix = expected_matrix / denominator

        kernel_matrix = self.kernel(strings, strings)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

    def test_two_sets(self):
        strings1 = np.array(["ATCG", "ATGG", "TACG"])
        strings2 = np.array(["ATCG", "GGGG", "CCCC"])
        expected_matrix = np.array([
            [4, 1, 1],
            [3, 2, 0],
            [2, 1, 1]
        ], dtype=float)

        n_rows = len(strings1)
        n_cols = len(strings2)
        for i in range(n_rows):
            for j in range(n_cols):
                denominator = math.sqrt(self.kernel.kernel_function(strings1[i], strings1[i]) *
                                        self.kernel.kernel_function(strings2[j], strings2[j]))
                expected_matrix[i, j] = expected_matrix[i, j] / denominator

        kernel_matrix = self.kernel(strings1, strings2)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

    def test_empty_strings(self):
        strings = np.array(["", "", ""])
        expected_matrix = np.zeros((3, 3))
        kernel_matrix = self.kernel(strings, strings)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

    def test_single_character_strings(self):
        strings = np.array(["A", "T", "A"])
        expected_matrix = np.array([
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ])

        denominator = expected_matrix[0, 0]
        expected_matrix = expected_matrix / denominator

        kernel_matrix = self.kernel(strings, strings)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)
    
    def test_performance(self):
        strings = np.array(["ATCGA" * 20] * 1000)  # 1000 sequences of length 100
        start_time = time.time()
        kernel_matrix = self.kernel(strings, strings)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Performance Test Duration: {duration:.4f} seconds")

if __name__ == '__main__':
    unittest.main()

"""
1000 sequences of length 100:
.Performance Test Duration: 5.1248 seconds
....
----------------------------------------------------------------------
Ran 5 tests in 5.156s

OK
"""
