/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <string.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>
#include "spectrum_sk.h"

double compute_spectrum_sk(char *str_a, char *str_b, 
                           bool use_sign)
{
    int32_t str_a_len = strlen(str_a);
    int32_t str_b_len = strlen(str_b);

    double result = 0;

    int32_t left_idx = 0;
    int32_t right_idx = 0;

    if (use_sign) {
        while (left_idx < str_a_len && right_idx < str_b_len) {
            if (str_a[left_idx] == str_b[right_idx]) {
                uint64_t sym = str_a[left_idx];

                while (left_idx < str_a_len && str_a[left_idx] == sym)
                    left_idx++;

                while (right_idx < str_b_len && str_b[right_idx] == sym)
                    right_idx++;

                result++;
            } else if (str_a[left_idx] < str_b[right_idx]) {
                left_idx++;
            } else {
                right_idx++;
            }
        }
    } else {
        while (left_idx < str_a_len && right_idx < str_b_len) {
            if (str_a[left_idx] == str_b[right_idx]) {
                int32_t old_left_idx = left_idx;
                int32_t old_right_idx = right_idx;

                uint64_t sym = str_a[left_idx];

                while (left_idx < str_a_len && str_a[left_idx] == sym)
                    left_idx++;

                while (right_idx < str_b_len && str_b[right_idx] == sym)
                    right_idx++;

                result += ((double) (left_idx - old_left_idx)) * ((double) (right_idx - old_right_idx));
            } else if (str_a[left_idx] < str_b[right_idx]) {
                left_idx++;
            } else {
                right_idx++;
            }
        }
    }

    return result;
}





#include <stdint.h>
#include <stdbool.h>

typedef double double;
typedef struct CStringFeatures {
    uint64_t* (*get_feature_vector)(struct CStringFeatures*, int32_t, int32_t*, bool*);
    void (*free_feature_vector)(struct CStringFeatures*, uint64_t*, int32_t, bool);
} CStringFeatures;

double calculate_similarity(CStringFeatures* lhs, int32_t idx_a, CStringFeatures* rhs, int32_t idx_b, bool use_sign) {

}






#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <math.h>

// Definições de estruturas e funções fictícias para substituições de C++
typedef struct {
    int num_symbols_in_histogram;
    int num_symbols;
    int num_bits;
} CAlphabet;

typedef struct {
    char* string;
    int slen;
} SGString;

typedef struct {
    int order;
    int num_vectors;
    int max_string_length;
    int original_num_symbols;
    long double num_symbols;
    SGString* features;
} CStringFeatures;

void remove_all_subsets(CStringFeatures* cf) {
    // Implementação fictícia
}

CAlphabet* get_alphabet(CStringFeatures* sf) {
    // Implementação fictícia
    return NULL;
}

void cleanup(CStringFeatures* cf) {
    // Implementação fictícia
}

int get_num_vectors(CStringFeatures* sf) {
    // Implementação fictícia
    return 0;
}

int get_max_vector_length(CStringFeatures* sf) {
    // Implementação fictícia
    return 0;
}

char* get_feature_vector(CStringFeatures* sf, int i, int* len, bool* vfree) {
    // Implementação fictícia
    return NULL;
}

void compute_symbol_mask_table(CStringFeatures* cf, int max_val) {
    // Implementação fictícia
}

void translate_from_single_order(char* fv, int len, int start_gap, int p_order_gap, int max_val, int gap) {
    // Implementação fictícia
}

void translate_from_single_order_reversed(char* fv, int len, int start_gap, int p_order_gap, int max_val, int gap) {
    // Implementação fictícia
}

bool obtain_from_char_features(CStringFeatures* cf, CStringFeatures* sf, int start,
                               int p_order, int gap, bool rev) {
    remove_all_subsets(cf);
    assert(sf != NULL);

    CAlphabet* alpha = get_alphabet(sf);
    assert(alpha->num_symbols_in_histogram > 0);

    cf->order = p_order;
    cleanup(cf);

    cf->num_vectors = get_num_vectors(sf);
    assert(cf->num_vectors > 0);
    cf->max_string_length = get_max_vector_length(sf) - start;
    cf->features = (SGString*)malloc(cf->num_vectors * sizeof(SGString));

    printf("%d symbols in StringFeatures<*> %d symbols in histogram\n", sf->num_symbols, alpha->num_symbols_in_histogram);

    for (int i = 0; i < cf->num_vectors; i++) {
        int len = -1;
        bool vfree;
        char* c = get_feature_vector(sf, i, &len, &vfree);
        assert(!vfree);

        cf->features[i].string = (char*)malloc(len * sizeof(char));
        cf->features[i].slen = len;

        char* str = cf->features[i].string;
        for (int j = 0; j < len; j++) {
            str[j] = (char)alpha->remap_to_bin(c[j]);
        }
    }

    cf->original_num_symbols = alpha->num_symbols;
    int max_val = alpha->num_bits;

    // SG_UNREF(alpha); // Não aplicável em C

    if (p_order > 1) {
        cf->num_symbols = powl(2, max_val * p_order);
    } else {
        cf->num_symbols = cf->original_num_symbols;
    }
    printf("max_val (bit): %d order: %d -> results in num_symbols: %.0Lf\n", max_val, p_order, (long double)cf->num_symbols);

    if ((long double)cf->num_symbols > powl(2, sizeof(char) * 8)) {
        printf("symbol does not fit into datatype \"%c\" (%d)\n", (char)max_val, max_val);
        return false;
    }

    printf("translate: start=%d order=%d gap=%d(size:%lu)\n", start, p_order, gap, sizeof(char));
    for (int line = 0; line < cf->num_vectors; line++) {
        int len = 0;
        bool vfree;
        char* fv = get_feature_vector(cf, line, &len, &vfree);
        assert(!vfree);

        if (rev) {
            translate_from_single_order_reversed(fv, len, start + gap, p_order + gap, max_val, gap);
        } else {
            translate_from_single_order(fv, len, start + gap, p_order + gap, max_val, gap);
        }

        // Ajuste do comprimento da string
        cf->features[line].slen -= start + gap;
        if (cf->features[line].slen < 0) {
            cf->features[line].slen = 0;
        }
    }

    compute_symbol_mask_table(cf, max_val);

    return true;
}
