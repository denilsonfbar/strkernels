
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import time
import numpy as np

# kernel class import
from sys import path
path.append('../..')
from strkernels import LocalityImprovedStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.kernel = LocalityImprovedStringKernel(length=0,
                                                   inner_degree=1,
                                                   outer_degree=1)

    def test_performance(self):

        # strings = np.array(["ATCGA" * 20] * 1000)  # 1000 sequences of length 100
        strings = np.array(["ATCGA" * 200] * 5000)  # 5000 sequences of length 1000

        start_time = time.time()
        kernel_matrix = self.kernel(strings, strings)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Performance test duration: {duration:.4f} seconds")

if __name__ == '__main__':
    unittest.main()

"""
5000 sequences of length 1000:

#pragma omp parallel for schedule(dynamic, 32)
Performance test duration: 59.7388 seconds
"""
