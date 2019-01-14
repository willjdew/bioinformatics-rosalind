# http://rosalind.info/problems/revc/

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.

import string

def complement_DNA(s):
    s.upper()
    trans_DNA = string.maketrans('ATCG', 'TAGC')
    sc = s.translate(trans_DNA)
    return sc
