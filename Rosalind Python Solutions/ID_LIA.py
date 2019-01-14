# http://rosalind.info/problems/lia/

# Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin
# with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children
# in the 1st generation, each of whom has two children, and so on. Each organism
# always mates with an organism having genotype Aa Bb.

# Return: The probability that at least N Aa Bb organisms will belong to the
# k-th generation of Tom's family tree (don't count the Aa Bb mates at each
# level). Assume that Mendel's second law holds for the factors

import math

# finds the number of possiblities for choosing an ordered set of r objects
# from a set of n objects
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def independent_alleles(k, n):
    # population size at generation k
    N = 2**k
    # probability set at 0
    prop = 0
    # for each generation in range n to N + 1
    for i in range(n, N+1):
        # find number of all possibilites of N at each generation
        f = nCr(N, i)
        # 
        prop = f*(0.25**i)*(0.75**(N-i)) + prop
    return prop
