/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#include <ctype.h>

// Define the possible alphabets
typedef enum {
  DNA,
  PROTEIN,
  ALPHANUMERIC
} AlphabetType;

// Function to generate all possible k-mers up to a given order for a specific alphabet.
char** generate_kmers(int order, int *num_kmers, AlphabetType alphabet_type) {
  char *bases;
  int num_bases;

  // Define the bases for each alphabet
  switch (alphabet_type) {
    case DNA:
      bases = "ACGT";
      num_bases = 4;
      break;
    case PROTEIN:
      bases = "ACDEFGHIKLMNPQRSTVWY";
      num_bases = 20;
      break;
    case ALPHANUMERIC:
      bases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
      num_bases = 36;
      break;
    default:
      fprintf(stderr, "Invalid alphabet type!\n");
      exit(1);
  }

  // Calculate the total number of k-mers.
  *num_kmers = 0;
  for (int i = 1; i <= order; ++i) {
    *num_kmers += pow(num_bases, i);
  }

  // Allocate memory for the k-mers.
  char **kmers = (char **)malloc(*num_kmers * sizeof(char *));
  if (kmers == NULL) {
    fprintf(stderr, "Memory allocation error!\n");
    exit(1);
  }

  int kmer_index = 0;

  // Generate k-mers of all orders from 1 up to 'order'.
  for (int i = 1; i <= order; ++i) {
    // Calculate the number of k-mers of this order.
    int num_kmers_i = pow(num_bases, i);

    // Allocate memory for each k-mer of this order.
    for (int j = 0; j < num_kmers_i; ++j) {
      kmers[kmer_index] = (char *)malloc((i + 1) * sizeof(char));
      if (kmers[kmer_index] == NULL) {
        fprintf(stderr, "Memory allocation error!\n");
        exit(1);
      }
      kmers[kmer_index][i] = '\0'; // Null-terminate the k-mer string.
      kmer_index++;
    }
  }

  // Construct the k-mers.
  kmer_index = 0;
  for (int i = 1; i <= order; ++i) {
    int num_kmers_i = pow(num_bases, i);

    for (int j = 0; j < num_kmers_i; ++j) {
      int temp = j;
      for (int l = i - 1; l >= 0; --l) {
        kmers[kmer_index][l] = bases[temp % num_bases];
        temp /= num_bases;
      }
      kmer_index++;
    }
  }

  return kmers;
}

// Function to count k-mer occurrences in a sequence (for any alphabet).
int* count_kmer_occurrences(const char *sequence, char **kmers, int num_kmers, int order) {
  int sequence_length = strlen(sequence);

  // Allocate memory for the k-mer counts.
  int *counts = (int *)calloc(num_kmers, sizeof(int)); // Initialize counts to 0
  if (counts == NULL) {
    fprintf(stderr, "Memory allocation error!\n");
    exit(1);
  }

  // Iterate through all possible k-mers in the sequence.
  for (int i = 0; i < sequence_length; ++i) {
      for (int k = 1; k <= order; ++k) {
        if (i + k <= sequence_length){
          // Extract the current k-mer.
          char current_kmer[k + 1];
          strncpy(current_kmer, sequence + i, k);
          current_kmer[k] = '\0';

          // Find the corresponding k-mer in the kmers array and increment its count.
          for (int j = 0; j < num_kmers; ++j) {
            if (strcmp(current_kmer, kmers[j]) == 0) {
              counts[j]++;
              break;
            }
          }
        }
      }
  }

  return counts;
}

// Function to calculate the inner product of two k-mer count vectors.
double calculate_inner_product(int *counts1, int *counts2, int num_kmers) {
  double inner_product = 0.0;
  for (int i = 0; i < num_kmers; ++i) {
    inner_product += counts1[i] * counts2[i];
  }
  return inner_product;
}

double compute_spectrum_sk(const char *str_a, const char *str_b, int32_t order, int32_t alphabet) {

    AlphabetType alphabet_type; 
    switch (alphabet){
        case 0:
            alphabet_type = DNA;        
            break;
        case 1:
            alphabet_type = PROTEIN;        
            break;
        case 2:
            alphabet_type = ALPHANUMERIC;        
            break;
        default:
            fprintf(stderr, "Invalid alphabet type!\n");
            exit(1);
    }

    // Generate all possible k-mers up to the given order for the chosen alphabet.
    int32_t num_kmers;
    char **kmers = generate_kmers(order, &num_kmers, alphabet_type);

    // Count the k-mer occurrences in the sequences.
    int32_t *counts_a = count_kmer_occurrences(str_a, kmers, num_kmers, order);
    int32_t *counts_b = count_kmer_occurrences(str_b, kmers, num_kmers, order);

    // Calculate the inner product of the two count vectors.
    double kernel_value = calculate_inner_product(counts_a, counts_b, num_kmers);

    // Free the allocated memory.
    for (int i = 0; i < num_kmers; ++i) {
        free(kmers[i]);
    }
    free(kmers);
    free(counts_a);
    free(counts_b);

    return kernel_value;
}
