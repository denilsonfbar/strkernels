/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <stdbool.h>
#include <stdint.h>
#include <omp.h>
#include "str_kernel_matrix.h"
#include "str_kernel.h"
#include "normalizer.h"

void compute_km(char **X_rows, char **X_cols, 
                int32_t X_rows_len, int32_t X_cols_len,
                bool symmetric,
                char *kernel_name,
                double param_1, double param_2, 
                double param_3, double param_4,
                char *normalizer,
                double **km)
{
    if (symmetric) {

        #pragma omp parallel for schedule(dynamic, 32)
        for (int32_t i = 0; i < X_rows_len; ++i) {
            for (int32_t j = 0; j <= i; ++j) {  // Only compute the lower triangular part of matrix
                km[i][j] = compute_kernel(X_rows[i], X_cols[j],
                                          kernel_name,
                                          param_1, param_2, 
                                          param_3, param_4);
            }
        }

        // Copy the lower triangular part to the upper triangular part
        #pragma omp parallel for schedule(dynamic, 32)
        for (int32_t i = 0; i < X_rows_len; ++i) {
            for (int32_t j = 0; j < i; ++j) {
                km[j][i] = km[i][j];
            }
        }

    } else {  // construct full matrix

        #pragma omp parallel for schedule(dynamic, 32)
        for (int32_t i = 0; i < X_rows_len; ++i) {
            for (int32_t j = 0; j < X_cols_len; ++j) {
                km[i][j] = compute_kernel(X_rows[i], X_cols[j],
                                          kernel_name,
                                          param_1, param_2, 
                                          param_3, param_4);
            }
        }
    }

    normalize(X_rows, X_cols, 
              X_rows_len, X_cols_len,
              symmetric,
              kernel_name,
              param_1, param_2, 
              param_3, param_4,
              normalizer,
              km);
}
