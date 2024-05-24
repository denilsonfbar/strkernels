
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


from abc import ABC, abstractmethod
import numpy as np
from concurrent.futures import ThreadPoolExecutor


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


    def compute_kernel_matrix_row(self, kernel_matrix, X_rows, X_cols, row_index, is_symmetric):
        """
        Compute an entire row of the kernel matrix.
        """
        for j in range(len(X_cols)):
            if is_symmetric and row_index > j:
                kernel_matrix[row_index, j] = kernel_matrix[j, row_index]
            else:
                kernel_matrix[row_index, j] = self.kernel_function(X_rows[row_index], X_cols[j])


    def __call__(self, X_rows, X_cols):
        """
        Compute the kernel matrix between strings in X_rows and X_cols,
        parallelizing the kernel function execution by row.

        Parameters:
            X_rows: ndarray or list of strings.
            X_cols: ndarray or list of strings.

        Returns:
            A float matrix of shape (len(X_rows), len(X_cols)).
        """
        if X_cols is X_rows:  # in training
            is_symmetric = True
        else:  # in prediction
            is_symmetric = False

        n_rows = len(X_rows)
        n_cols = len(X_cols)
        kernel_matrix = np.zeros((n_rows, n_cols))

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(
                self.compute_kernel_matrix_row, kernel_matrix, X_rows, X_cols, i, is_symmetric) 
                for i in range(n_rows)]
            
            # wait for all tasks to complete
            for future in futures:
                future.result()

        return kernel_matrix


    def __str__(self):
        str_ret = str(self._kernel_name)
        if self._kernel_params:
            str_ret += ' ' + str(self._kernel_params)
        return str_ret


    def __repr__(self):
        return self.__str__()
