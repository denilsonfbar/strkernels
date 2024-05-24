
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import numpy as np
import math


def normalize(normalizer, X_rows, X_cols, kernel_function, kernel_matrix, is_symmetric):

    if normalizer == 'sqrt_diagonal':
        sqrt_diagonal_kernel_normalizer(X_rows, X_cols, kernel_function, kernel_matrix, is_symmetric)


def sqrt_diagonal_kernel_normalizer(X_rows, X_cols, kernel_function, kernel_matrix, is_symmetric):

    n_rows = len(X_rows)
    n_cols = len(X_cols)

    if not is_symmetric:
        X_rows_self_kernel = np.array([kernel_function(X_rows[i], X_rows[i]) for i in range(n_rows)])
        X_cols_self_kernel = np.array([kernel_function(X_cols[j], X_cols[j]) for j in range(n_cols)])

    normalized_kernel_matrix = np.zeros((n_rows, n_cols))

    for i in range(n_rows):
        for j in range(n_cols):

            if is_symmetric:  # k(x,x) are the diagonal values
                denominator = math.sqrt(kernel_matrix[i, i] * kernel_matrix[j, j])
            else:
                denominator = math.sqrt(X_rows_self_kernel[i] * X_cols_self_kernel[j])
            if denominator == 0.0: 
                denominator = np.finfo(np.float64).min

            normalized_kernel_matrix[i, j] = kernel_matrix[i, j] / denominator

    kernel_matrix = normalized_kernel_matrix
