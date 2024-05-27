
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import numpy as np

from .string_kernel import StringKernel


class SubsequenceStringKernel(StringKernel):
    """
    Subsequence string kernel.
    """

    def __init__(self, normalizer='sqrt_diagonal', **kernel_params):
        """
        Kernel constructor.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        # specific kernel parameter
        if 'maxlen' not in kernel_params:
            kernel_params['ssk_maxlen'] = 3  # default maxlen value
        if 'lambda' not in kernel_params:
            kernel_params['ssk_lambda'] = 0.5  # default lambda value

        super().__init__(**kernel_params)  # base class constructor
        self._kernel_name = 'SubsequenceStringKernel'


    def kernel_function(self, str_a, str_b):
        """
        Subsequence string kernel.

        Parameters:
            str_a (string)
            str_b (string)

        Returns:
            float: the result of kernel function.
        """
        ssk_maxlen = self._kernel_params['ssk_maxlen']
        ssk_lambda = self._kernel_params['ssk_lambda']

        alen = len(str_a)
        blen = len(str_b)

        # allocating memory to compute K' (Kp)
        Kp = np.zeros((ssk_maxlen+1, alen, blen))

        # initialize for 0 subsequence length for both strings
        Kp[0, :, :] = 1.0

        # computing the K' (Kp) function using equations shown in Lodhi et al. (2002)
        for i in range(ssk_maxlen):
            for j in range(alen-1):
                Kpp = 0.0
                for k in range(blen-1):
                    Kpp = ssk_lambda * (Kpp + ssk_lambda * (str_a[j] == str_b[k]) * Kp[i, j, k])
                    Kp[i+1, j+1, k+1] = ssk_lambda * Kp[i+1, j, k+1] + Kpp

        # compute the kernel function
        kernel_value = 0.0
        for i in range(ssk_maxlen):
            for j in range(alen):
                for k in range(blen):
                    kernel_value += ssk_lambda * ssk_lambda * (str_a[j] == str_b[k]) * Kp[i, j, k]

        return kernel_value
