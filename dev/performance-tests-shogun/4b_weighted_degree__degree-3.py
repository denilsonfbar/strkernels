
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import time
import numpy as np

from shogun import StringCharFeatures, DNA
from shogun import SqrtDiagKernelNormalizer
from shogun import WeightedDegreeStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.normalizer = SqrtDiagKernelNormalizer()
        self.degree = 3


    def test_performance(self):

        # strings = np.array(["ATCGA" * 20] * 1000)  # 1000 sequences of length 100
        strings = np.array(["ATCGA" * 200] * 5000)  # 5000 sequences of length 1000

        start_time = time.time()
	    
        shogun_feats = StringCharFeatures(strings.tolist(), DNA)
        kernel = WeightedDegreeStringKernel(shogun_feats, shogun_feats, self.degree)
        kernel.set_normalizer(self.normalizer)
        kernel_matrix = kernel.get_kernel_matrix()

        end_time = time.time()
        duration = end_time - start_time
        print(f"Performance test duration: {duration:.4f} seconds")

if __name__ == '__main__':
    unittest.main()

"""
5000 sequences of length 1000:

strkernels v0.1.0 local compilation:
Performance test duration: 69.7939 seconds

Shogun 6.1.3:
Performance test duration: 1.2300 seconds
"""
