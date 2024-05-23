
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


from abc import ABC, abstractmethod
from .libshogun.shogun import StringCharFeatures


class StringKernel(ABC):
    """
    Base class to represent a string kernel.
    """

    def __init__(self, alphabet=None, **kernel_params):
        """
        Constructor for attributes and parameters definition.
        """
        # general attributes
        self._kernel_name = None
        self._alphabet = alphabet  # 'DNA', 'RNA', 'protein', 'rawbyte'
        self._kernel_params = {}  # kernel parameters dictionary

        # features objects of Shogun toolbox
        self._X_left_sg = None
        self._X_right_sg = None

        # kernel object of Shogun toolbox
        self._kernel_sg = None

        # set or update kernel parameters
        if kernel_params:
            self.set_params(**kernel_params)


    def set_params(self, **kernel_params):
        """
        Set or update kernel parameters.
        """
        for key, value in kernel_params.items():
            self._kernel_params[key] = value


    @abstractmethod
    def __call__(self, X_left, X_right, alphabet=None, **kernel_params):
        """
        Compute the kernel matrix between strings  
        in X_left and X_right collections.

        Parameters:
            X_left: ndarray or list of strings of len == n_samples in X_left.
            X_right: ndarray or list of strings of len == n_samples in X_right.

        Returns:
            A real kernel matrix of shape (len(X_left), len(X_right)).
        """
        if alphabet is not None:
            self._alphabet = alphabet  # 'DNA', 'RNA', 'protein', 'rawbyte'

        # set or update kernel parameters
        if kernel_params:
            self.set_params(**kernel_params)

        ## Create Shogun features objects
        #
        if self._alphabet is None:  # TODO: detect alphabet and update self._alphabet
            raise ValueError("Alphabet is not defined.")  

        if self._alphabet == 'DNA':
            from .libshogun.shogun import DNA
            alphabet_sg = DNA

        self._X_left_sg = StringCharFeatures(X_left, alphabet_sg)
        if X_right == X_left:  # in training are
            self._X_right_sg = self._X_left_sg
        else:
            self._X_right_sg = StringCharFeatures(X_right, alphabet_sg)


    def __str__(self):
        str_ret = str(self._kernel_name)
        if self._kernel_params:
            str_ret += ' ' + str(self._kernel_params)
        return str_ret

    def __repr__(self):
        return self.__str__()
