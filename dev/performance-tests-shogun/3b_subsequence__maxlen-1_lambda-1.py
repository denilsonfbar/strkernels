
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import time
import numpy as np

from shogun import StringCharFeatures, DNA
from shogun import SqrtDiagKernelNormalizer
from shogun import SubsequenceStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.normalizer = SqrtDiagKernelNormalizer()
        self.maxlen = 1
        self.ssk_lambda = 1.0


    def test_performance(self):

        strings = np.array(["ATCGA" * 20] * 1000)  # 1000 sequences of length 100
        # strings = np.array(["ATCGA" * 200] * 5000)  # 5000 sequences of length 1000

        start_time = time.time()
	    
        shogun_feats = StringCharFeatures(strings.tolist(), DNA)
        kernel = SubsequenceStringKernel(shogun_feats, shogun_feats, self.maxlen, self.ssk_lambda)
        kernel.set_normalizer(self.normalizer)
        kernel_matrix = kernel.get_kernel_matrix()

        end_time = time.time()
        duration = end_time - start_time
        print(f"Performance test duration: {duration:.4f} seconds")

if __name__ == '__main__':
    unittest.main()

"""
1000 sequences of length 100:

strkernels v0.1.0 from pip:
Performance test duration: 4.1049 seconds

Shogun 6.1.3:
Performance test duration: 3.9218 seconds
"""
