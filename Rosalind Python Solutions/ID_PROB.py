# http://rosalind.info/problems/prob/

# Given: A DNA string s of length at most 100 bp and an array A containing at
# most 20 numbers between 0 and 1.

# Return: An array B having the same length as A in which B[k] represents the
# common logarithm of the probability that a random string constructed with the
# GC-content found in A[k] will match s exactly.

import math

# counts the number of each base
def counting_DNA_Nucleotides(s):
    s = s.upper()
    A = s.count('A')
    C = s.count('C')
    G = s.count('G')
    T = s.count('T')

    return A, C, G, T

# finds the AT and GC counts
def AT_GC_counts(seq):
    A, C, G, T= counting_DNA_Nucleotides(seq)
    AT = A + T
    GC = G + C
    return AT, GC

# retuns the log10 of the probabilities of AT and GC given a gc content
def log_10_probabilites(value, AT, GC):
    return round(math.log10((((1 - value) / 2)**AT) * (value / 2)**GC), 3)

def probabilities(gc_content, seq):
    # finds the AT and GC counts
    AT, GC = AT_GC_counts(seq)
    probabilities = []
    # for each gc_content given
    for i in gc_content:
        # retuns the log10 of the probabilities of AT and GC given a gc content
        prob = log_10_probabilites(i, AT, GC)
        probabilities.append(prob)
    return probabilities
