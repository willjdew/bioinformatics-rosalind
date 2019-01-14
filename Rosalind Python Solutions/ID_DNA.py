# Counting DNA Nucleotides
# http://rosalind.info/problems/dna/

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of
# times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def counting_DNA_Nucleotides(s):
    s = s.upper()
    A = s.count('A')
    C = s.count('C')
    G = s.count('G')
    T = s.count('T')

    return A, C, G, T
