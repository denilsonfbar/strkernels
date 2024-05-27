/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <string.h>
#include <stdint.h>
#include "str_kernel.h"
#include "fixed_degree_sk.h"
#include "subsequence_sk.h"

double compute_kernel(char *str_a, char *str_b,
                      char *kernel_name,
                      double param_1, double param_2, 
                      double param_3, double param_4)
{
    if (strcmp(kernel_name, "FixedDegreeStringKernel") == 0) 
    {
        int32_t degree = (int32_t) param_1;
        return (double)compute_fixed_degree_sk(str_a, str_b, degree);
    } 
    else if (strcmp(kernel_name, "SubsequenceStringKernel") == 0) 
    {
        int32_t maxlen = (int32_t) param_1;
        double lambda = param_2;
        return compute_subsequence_sk(str_a, str_b, maxlen, lambda);
    } 
}    