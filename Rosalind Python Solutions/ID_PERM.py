# http://rosalind.info/problems/perm/

# Given: A positive integer n≤7.

# Return: The total number of permutations of length n, followed by a list of
# all such permutations (in any order).

from itertools import permutations

def permutation_n(n):
    l = []
    # for i in range n + 1 for exclution of 0.
    for i in range(1,n+1):
        l.append(i)
    # use permutations funciton to find all permutations
    perm = permutations(l)

    return list(perm)
