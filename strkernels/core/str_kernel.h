/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#ifndef STR_KERNEL_H
#define STR_KERNEL_H

#include <string.h>
#include <stdint.h>
#include "fixed_degree_sk.h"

double compute_kernel(char *str_a, char *str_b,
                      char *kernel_name,
                      double param_1, double param_2, 
                      double param_3, double param_4)
{
    if (strcmp(kernel_name, "FixedDegreeStringKernel") == 0) 
    {
        int32_t degree = int32_t(param_1);
        return (double)compute_fixed_degree_sk(str_a, str_b, degree);
    } 
/*    else if (strcmp(kernel_name, "SubsequenceStringKernel") == 0) 
    {
        return (double)compute_subsequence_sk();
    } 
*/
}    

#endif
