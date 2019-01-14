# http://rosalind.info/problems/revp/

# Given: A DNA string of length at most 1 kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the string
# having length between 4 and 12. You may return these pairs in any order.

# Split the file contents at '>' to get a list of strings representing entries
def read_FASTA_strings(filename):
    with open(filename) as file:
        return file.read().split('>')[1:]

# Partition the strings to seperate the first line from the rest
def read_FASTA_entries(filename):
    return [seq.partition('\n') for seq in read_FASTA_strings(filename)]

# Remove the newlines from the sequence data
def read_FASTA_sequences(filename):
    return [(info[0:], seq.replace('\n', ''))
            for info, ignore, seq in #ignor is ignores (!)
            read_FASTA_entries(filename)]

# Create an sequence dictionary from sequence data
def make_indexed_sequences_dictionary(filename):
    return {info: seq for info, seq in read_FASTA_sequences(filename)}

import string

# Creates a compliment strand
def complement_dna(s):
    s.upper()
    # returns a translation table that maps each character in the
    # intabstring into the character at the same position in the outtab
    # string. Then this table is passed to the translate() function.
    trans_dna = string.maketrans('ATCG', 'TAGC')
    sc = s.translate(trans_dna)
    return sc

def palindrome(dna):
    # Creates a compliment strand
    cdna = complement_DNA(dna)
    store = []
    len_range = [12, 11, 10, 9, 8, 7, 6, 5, 4]
    # for each lenght in len_range
    for n in len_range:
        # for each position in range of length of dna
        for i in range(len(dna)):
            # if i is greater then length of dna minus n break the loop
            if i > len(dna) - n:
                break
            else:
                # if i is less than lenght of dna minus n. complement sequence
                # slice is compaired to dna at position i + range n
                q = cdna[i:i+n]
                if dna[i:i+n] == q[::-1]:
                    # if sequences are the same then make positions and store in
                    # list store to return
                    pos = (i+1, n)
                    store.append(pos)
    return store
