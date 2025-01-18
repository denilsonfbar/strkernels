/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <string.h>
#include <stdbool.h>
#include <stdint.h>
#include "weighted_degree_sk.h"

int64_t compute_weighted_degree_sk(char *str_a, char *str_b, int32_t degree) 
{
    int32_t str_a_len = strlen(str_a);
    int32_t str_b_len = strlen(str_b);
    	
	// Accept strings with different lengths
	int32_t shortest_str_len = (str_a_len < str_b_len) ? str_a_len : str_b_len;

    int64_t kernel_value = 0;
	for (int32_t k=1; k < degree+1; k++){

		int32_t w = degree - k + 1;
		int64_t degree_kernel_value = 0;

		for (int32_t i=0; i < shortest_str_len-k+1; i++)
		{
			bool match = true;

			for (int32_t j=i; j < i+k && match; j++)
				match = str_a[j]==str_b[j];

			if (match)
				degree_kernel_value++;
		}
        kernel_value += (degree_kernel_value * w);
	}
    return kernel_value;
}
