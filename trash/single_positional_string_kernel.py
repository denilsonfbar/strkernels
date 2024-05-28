
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


from .string_kernel import StringKernel


class SinglePositionalStringKernel(StringKernel):
    """
    Single Positional string kernel counts the number of common characters 
    in the same positions between two strings.
    """

    def __init__(self, **kernel_params):
        """
        Kernel constructor.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        super().__init__(**kernel_params)  # base class constructor
        self._kernel_name = 'SinglePositionalStringKernel'


    def kernel_function(self, str_a, str_b):
        """
        Counts the number of common characters in the same positions between two strings.

        Parameters:
            str_a (string)
            str_b (string)

        Returns:
            float: the result of kernel function.
        """
        return sum(1 for a, b in zip(str_a, str_b) if a == b)
