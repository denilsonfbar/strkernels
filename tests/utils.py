
# Author: Denilson Fagundes Barbosa <denilsonfbar@gmail.com>


import numpy as np


def generate_random_dna_str(seq_len, random_seed=None):

    if random_seed is not None:
        np.random.seed(random_seed)

    return ''.join(np.random.choice(['A', 'C', 'G', 'T'], size=seq_len))


def generate_random_dna_str_list(n_seqs, seq_len, random_seed=None):

    if random_seed is not None:
        np.random.seed(random_seed)
    
    dna_seqs = []
    for _ in range(n_seqs):
        dna_seqs.append(generate_random_dna_str(seq_len))

    return dna_seqs


def generate_random_binary_labels(n_labels, random_seed=None):

    if random_seed is not None:
        np.random.seed(random_seed)
    
    return np.random.choice([-1, 1], size=n_labels)
