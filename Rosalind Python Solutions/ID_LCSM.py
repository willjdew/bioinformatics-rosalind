# http://rosalind.info/problems/lcsm/

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in
# FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions
# exist, you may return any single solution.)

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

# Find the longest substring
def longest_common_substring(s1, s2):
    # create a matrix filled with -1 the is len(s1) x len(s2)
    m = [[-1] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    # going through the matrix a row at a time
    for x in xrange(1, 1 + len(s1)):
        # going through the matrix a column at a time
        for y in xrange(1, 1 + len(s2)):
            # if charater (s1[x - 1]) equals charater (s2[y - 1])
            if s1[x - 1] == s2[y - 1]:
                # change the related place in matrix to plus one
                m[x][y] = m[x - 1][y - 1] + 1
                # if matrix value is longer than previous longest set
                # longest = m[x][y] and x_longest = x
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            # if the characters don't match set matrix value to 0
            else:
                m[x][y] = 0
    # return slice of string s1[x_longest - longest: x_longest]
    return s1[x_longest - longest: x_longest]


def finding_shared_motif(filename):
    # get fasta dictionary
    d = make_indexed_sequences_dictionary(filename)
    # create list of fasta dict keys
    lcs_keys = list(d.keys())
    lcs = d[lcs_keys[0]]
    # for keys in lcs_keys starting with the second key
    for i in range(1,len(lcs_keys)):
        # set lcs to the previous lcs and the next lcs key.
        lcs = longest_common_substring(lcs, d[lcs_keys[i]])
    return lcs
