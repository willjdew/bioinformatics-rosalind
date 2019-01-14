# http://rosalind.info/problems/pper/

# Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

# Return: The total number of partial permutations P(n,k), modulo 1,000,000.

import math

def partial_permutation(n, k, modulo=None):
    # For k items out of n, the number of k-permutations is equal to n!/(n−k)!
    n_fact = math.factorial(n)
    n_k_fact = math.factorial(n-k)

    return n_fact / n_k_fact % modulo
