
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import time
import numpy as np

from shogun import StringCharFeatures, DNA
from shogun import SqrtDiagKernelNormalizer
from shogun import FixedDegreeStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.normalizer = SqrtDiagKernelNormalizer()
        self.degree = 1


    def test_performance(self):

        # strings = np.array(["ATCGA" * 20] * 1000)  # 1000 sequences of length 100
        strings = np.array(["ATCGA" * 200] * 5000)  # 5000 sequences of length 1000

        start_time = time.time()
	    
        shogun_feats = StringCharFeatures(strings.tolist(), DNA)
        kernel = FixedDegreeStringKernel(shogun_feats, shogun_feats, self.degree)
        kernel.set_normalizer(self.normalizer)
        kernel_matrix = kernel.get_kernel_matrix()

        end_time = time.time()
        duration = end_time - start_time
        print(f"Performance test duration: {duration:.4f} seconds")

if __name__ == '__main__':
    unittest.main()

"""
5000 sequences of length 1000:

#pragma omp parallel for schedule(dynamic, 32)
Performance test duration: 12.3674 seconds

strkernels v0.1.0 from pip:
Performance test duration: 2.4190 seconds

Shogun 6.1.3:
Performance test duration: 3.6400 seconds
"""
