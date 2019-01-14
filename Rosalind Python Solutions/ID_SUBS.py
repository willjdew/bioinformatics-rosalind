# http://rosalind.info/problems/subs/

# Given: Two DNA strings s and t (each of length at most 1 kbp).

# Return: All locations of t as a substring of s.

import re

def find_motif(motif, seq):
    # create lookahead string to find overlapping motifs
    q = '(?=' + motif + ')'
    # create iterator to find all the motifs in the seq
    iterator = re.finditer(q, seq)
    # find all start locations of motifs in the seq
    indices = [m.start(0) for m in iterator]
    # make start locations of indices for base 1
    indices_base_1 = [x+1 for x in indices]

    return indices_base_1
