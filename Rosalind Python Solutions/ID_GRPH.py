# http://rosalind.info/problems/grph/

# Given: A collection of DNA strings in FASTA format having total length at
# most 10 kbp.

# Return: The adjacency list corresponding to O3. You may return edges in any
# order.

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

# create prefix and suffix dictionary
def dna_pre_suf(k, key, value):
    r = {}
    r['name'] = key
    r['dna'] = value
    r['kprefix'] = value[0:k]
    r['ksuffix'] = value[-k:]
    r['overlap'] = []
    return r

# create dictionary for all prefix and suffix dictionaries
def make_og_dict(dna_dict, k):
    og = {}
    for key in dna_dict.keys():
        og[key] = dna_pre_suf(k, key, dna_dict[key])
    return og

# compares the suffix of and prefix of two dictionaires
def compare_suffix_prefix(one, two):
    # create strings for each thing being comparies
    one_name, two_name = one['name'], two['name']
    one_dna, two_dna = one['dna'], two['dna']
    one_ksuffix, two_kprefix = one['ksuffix'], two['kprefix']

    # If name or dna sequence is the same return nothing. If one suffix is same
    # as two prefix return two name.
    if one_name == two_name:
        return
    elif one_dna == two_dna:
        return
    elif one_ksuffix == two_kprefix:
        return two_name
    else:
        return

def make_overlap_graph_dict(filename, k):
    # create dna_dict from fasta file
    dna_dict = make_indexed_sequences_dictionary(filename)

    # create dictionary for all prefix and suffix dictionaries and list of
    # dictionary keys
    og = make_og_dict(dna_dict, k)
    og_list = list(og)

    # for each dna key in og dictioanry will be suffix will be compared to each
    # other dna key's prefix.  If they are a match the name of the prefix dna
    # will be added to the suffix dna overlap key.
    for n in range(len(og_list)):
        one = og_list[n]
        for l in og_list:
            suf_pre = compare_suffix_prefix(og[one], og[l])
            if suf_pre:
                pointer_dict = og[one]
                pointer_dict['overlap'].append(suf_pre)

    return og
