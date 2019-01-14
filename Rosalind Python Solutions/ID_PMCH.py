# http://rosalind.info/problems/pmch/

# Given: An RNA string s of length at most 80 bp having the same number of
# occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

# Return: The total possible number of perfect matchings of basepair edges in
# the bonding graph of s.

import math

# counts the number of nucleotides in dna sequence
def counting_RNA_Nucleotides(s):
    s = s.upper()
    A = s.count('A')
    C = s.count('C')
    G = s.count('G')
    U = s.count('U')

    return A, C, G, U

def perfect_matching(s):
    # counts the number of nucleotides in dna sequence
    A, C, G, U = counting_RNA_Nucleotides(s)

    # for a perfect matching of rna nuceotides to occur you need the same amount
    # of A to U and G to C.
    if (A != U):
        return 'Not same number of A and U occurrences'
    elif G != C:
        return 'Not same number of G and C occurrences'
    # if there is same amount of nuceotides then find the factorial of A and G
    # and return the factorials multiplied
    else:
        a_fact = math.factorial(A)
        g_fact = math.factorial(G)

        return a_fact * g_fact
