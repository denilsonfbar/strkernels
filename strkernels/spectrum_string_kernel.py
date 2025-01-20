
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import numpy as np

from .string_kernel import StringKernel


class SpectrumStringKernel(StringKernel):
    """
    Spectrum string kernel.
    """

    def __init__(self, normalizer='sqrt_diagonal', **kernel_params):
        """
        Kernel constructor.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        super().__init__()  # base class constructor

        # kernel name
        self._kernel_name = 'SpectrumStringKernel'

        # specific kernel parameter
        if 'order' not in kernel_params:
            kernel_params['order'] = 3  # default order value
        if 'alphabet' not in kernel_params:
            kernel_params['alphabet'] = 0  # 0: DNA, 1: Protein, 2: Alphanumeric

        # set kernel parameters
        self.set_params(**kernel_params)
        
        # set normalizer
        self._normalizer = normalizer


    def set_params(self, **kernel_params):

        super().set_params(**kernel_params)

        # ctypes parameters conversion
        self._param_1 = np.float64(self._kernel_params['order'])
        self._param_2 = np.float64(self._kernel_params['alphabet']) 
        self._param_3 = 0.0
        self._param_4 = 0.0
