
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import time
import numpy as np

from shogun import StringCharFeatures, DNA
from shogun import SqrtDiagKernelNormalizer
from shogun import StringUlongFeatures, CommUlongStringKernel, SortUlongString


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.normalizer = SqrtDiagKernelNormalizer()
        self.order = 3
        self.gap = 0
        self.reverse = False
        self.use_sign = False


    def test_performance(self):

        strings = np.array(["ATCGA" * 20] * 1000)  # 1000 sequences of length 100
        # strings = np.array(["ATCGA" * 200] * 5000)  # 5000 sequences of length 1000

        start_time = time.time()
	    
        shogun_feats = StringCharFeatures(strings.tolist(), DNA)

        ulong_shogun_feats = StringUlongFeatures(shogun_feats.get_alphabet())
        ulong_shogun_feats.obtain_from_char(shogun_feats, self.order-1, self.order, 
                                            self.gap, self.reverse)

        preproc = SortUlongString()
        preproc.init(ulong_shogun_feats)
        ulong_shogun_feats.add_preprocessor(preproc)
        ulong_shogun_feats.apply_preprocessor()

        kernel = CommUlongStringKernel(ulong_shogun_feats, ulong_shogun_feats, self.use_sign)
        kernel.set_normalizer(self.normalizer)
        kernel_matrix = kernel.get_kernel_matrix()

        end_time = time.time()
        duration = end_time - start_time
        print(f"Performance test duration: {duration:.4f} seconds")

if __name__ == '__main__':
    unittest.main()

"""
1000 sequences of length 100:

strkernels v0.1.0 local compilation:
Performance test duration: 5.4299 seconds

Shogun 6.1.3:
Performance test duration: 0.1125 seconds
"""
