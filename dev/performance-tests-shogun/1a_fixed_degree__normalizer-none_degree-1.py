
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import time
import numpy as np

from shogun import StringCharFeatures, DNA
from shogun import IdentityKernelNormalizer
from shogun import FixedDegreeStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.normalizer = IdentityKernelNormalizer()  # no normalization is applied
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
1000 sequences of length 100:

Python kernel implementation: 
Performance test duration: 4.8814 seconds

C kernel implementation:
Performance test duration: 0.2006 seconds


5000 sequences of length 1000:

C kernel implementation:
Performance Test Duration: 44.0703 seconds

#pragma omp parallel for
Performance test duration: 14.1806 seconds

#pragma omp parallel for schedule(static)
Performance test duration: 13.6119 seconds

#pragma omp parallel for collapse(2)
Performance test duration: 12.4508 seconds

#pragma omp parallel for schedule(dynamic, 32)
Performance test duration: 11.8082 seconds

strkernels v0.1.0 from pip:
Performance test duration: 2.2458 seconds

Shogun 6.1.3:
Performance test duration: 3.5803 seconds
"""
