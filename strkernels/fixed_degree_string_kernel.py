
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


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
        self._kernel_name = 'FixedDegreeStringKernel'


    def kernel_function(self, str_a, str_b):
        """
        Fixed Degree string kernel.

        Parameters:
            str_a (string)
            str_b (string)

        Returns:
            float: the result of kernel function.
        """
        
        degree = self._kernel_params['degree']
        shortest_string_len = min(len(str_a), len(str_b))
        kernel_value = 0

        for i in range(shortest_string_len-degree+1):
            match = True

            for j in range(i, i+degree):
                if match:
                    match = str_a[j] == str_b[j]
                else:
                    break

            if match:
                kernel_value += 1

        return kernel_value
