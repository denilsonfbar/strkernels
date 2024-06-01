
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import time
import numpy as np

# kernel class import
from sys import path
path.append('..')
from strkernels import LocalityImprovedStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.kernel = LocalityImprovedStringKernel(normalizer=None, 
                                                   length=3,
                                                   inner_degree=2,
                                                   outer_degree=1)

    def test_single_set(self):
        strings = np.array(["ATCG", "ATGG", "TACG", "GCTA"])
        expected_matrix = np.array([
            [4, 3, 2, 0],
            [3, 4, 1, 0],
            [2, 1, 4, 0],
            [0, 0, 0, 4]
        ])
        kernel_matrix = self.kernel(strings, strings)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

    def test_two_sets(self):
        strings1 = np.array(["ATCG", "ATGG", "TACG"])
        strings2 = np.array(["ATCG", "GGGG", "CCCC"])
        expected_matrix = np.array([
            [4, 1, 1],
            [3, 2, 0],
            [2, 1, 1]
        ])
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

"""
