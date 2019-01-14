# http://rosalind.info/problems/mrna/

# Given: A protein string of length at most 1000 aa.

# Return: The total number of different RNA strings from which the protein
# could have been translated, modulo 1,000,000. (Don't neglect the importance
# of the stop codon in protein translation.)

from functools import reduce
from operator import mul

def num_rna_strings(dna, modulo=None):
    # frequency of Ammio acids table
    freq = {'A': 4, 'C': 2, 'D': 2, 'E': 2,
            'F': 2, 'G': 4, 'H': 2, 'I': 3,
            'K': 2, 'L': 6, 'M': 1, 'N': 2,
            'P': 4, 'Q': 2, 'R': 6, 'S': 6,
            'T': 4, 'V': 4, 'W': 1, 'Y': 2,
            'STOP': 3
            }

    # if modulo is True then assign a*b % modulo function to reduce_fn
    if modulo:
        reduce_fn = lambda a, b: (a * b) % modulo
    # else assign mul multiplier function to reduce_fn
    else:
        reduce_fn = mul

    # freq is the generator for frequency table for each base in dna
    freqs = (freq[base] for base in dna)

    # applies reduce_fn function to all freq[base] in dna and stops at
    # freq['STOP']
    return reduce(reduce_fn, freqs, freq["STOP"])
