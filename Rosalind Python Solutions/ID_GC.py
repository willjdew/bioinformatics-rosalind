# http://rosalind.info/problems/gc/

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the
# GC-content of that string. Rosalind allows for a default error of 0.001 in all
# decimal answers unless otherwise stated; please see the note on absolute error
# below.

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

# Counts GC bases and returns percentage
def gc_content(base_sequence):
    # make base_sequence a string and Upper case for uniform processing.
    base_sequence = str(base_sequence)
    seq = base_sequence.upper()
    # Count G and C and return percentage
    g = float(seq.count('G'))
    c = float(seq.count('C'))
    l = float(len(seq))
    return (g + c) / l * 100

# Creates a dictionary for each sequence of the GC content
def gc_content_dict(fasta_dict):
    gc_dict = {}
    # for each sequence in fasta_dict find the gc content and create new dict
    for key in fasta_dict.keys():
        gc_dict[key] = gc_content(fasta_dict[key]) * 100
    return gc_dict

# Finds the max value in a dictionary
def key_with_max_val(d):
    # create a list of the dict's keys and values;
    v=list(d.values())
    k=list(d.keys())
    # return the key with the max value
    return k[v.index(max(v))]

# Given a fasta file returns the sequence with the max GC content
def highest_gc_content(filename):
    # Create an sequence dictionary from sequence data in filename
    fasta_dict = make_indexed_sequences_dictionary(filename)
    # Create a gc content dictionary
    gc_dict = gc_content_dict(fasta_dict)
    # find the sequence with the largest gc content
    max_key = key_with_max_val(gc_dict)
    # return key name and gc_content value
    return max_key, gc_dict[max_key]
