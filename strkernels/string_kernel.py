
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


from abc import ABC, abstractmethod


class StringKernel(ABC):
    """
    Base class to represent a string kernel.
    """

    def __init__(self, **kernel_params):
        """
        Constructor with attributes and kernel parameters definition.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        self._kernel_name = None
        self._kernel_params = {}

        # set kernel parameters
        if kernel_params:
            self.set_params(**kernel_params)


    def set_params(self, **kernel_params):
        """
        Set or update kernel parameters.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        for key, value in kernel_params.items():
            self._kernel_params[key] = value


    @abstractmethod
    def kernel_function(self, str_a, str_b):
        """
        Calculate the kernel function between two strings.

        Parameters:
            str_a (string)
            str_b (string)

        Returns:
            float: the result of kernel function.
        """


    def __call__(self, X_left, X_right):
        """
        Compute the kernel matrix between strings in X_left and X_right.

        Parameters:
            X_left: ndarray or list of strings.
            X_right: ndarray or list of strings.

        Returns:
            A float matrix of shape (len(X_left), len(X_right)).
        """


    def __str__(self):
        str_ret = str(self._kernel_name)
        if self._kernel_params:
            str_ret += ' ' + str(self._kernel_params)
        return str_ret


    def __repr__(self):
        return self.__str__()
