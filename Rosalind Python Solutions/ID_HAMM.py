# http://rosalind.info/problems/hamm/

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).

def hamming_distance(seq1, seq2):
    # Check to see if sequences are of equal length
    if len(seq1) != len(seq2):
        raise ValueError("Undefined for sequences of unequal length")
    # returns sum of the differences in sequences when seq1 and seq2 are zip()
    return sum(aa1 != aa2 for aa1, aa2 in zip(seq1, seq2))
