
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import numpy as np

from .string_kernel import StringKernel


class FixedDegreeStringKernel(StringKernel):
    """
    Fixed Degree string kernel.
    """

    def __init__(self, **kernel_params):
        """
        Kernel constructor.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        # specific kernel parameter
        if 'degree' not in kernel_params:
            kernel_params['degree'] = 3  # default degree value

        super().__init__(**kernel_params)  # base class constructor
        
        # adjusting attributes
        self._kernel_name = 'FixedDegreeStringKernel'
        self._param_1 = np.float64(self._kernel_params['degree'])
        self._param_2 = 0.0 
        self._param_3 = 0.0
        self._param_4 = 0.0
