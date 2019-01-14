# http://rosalind.info/problems/mprt/

# Given: At most 15 UniProt Protein Database access IDs.

# Return: For each protein possessing the N-glycosylation motif, output its
# given access ID followed by a list of locations in the protein string where
# the motif can be found.

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

def find_protein_motifs(filename, motif):
    motif_dict = make_indexed_sequences_dictionary(filename)
    loc_motif_dict = {}

    for k in motif_dict.keys():
        loc_motif_dict[k] = find_motif(motif, motif_dict[k])

    return loc_motif_dict
