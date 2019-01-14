# http://rosalind.info/problems/cons/

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
# in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several
# possible consensus strings exist, then you may return any one of them.)

import pandas as pd

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

# takes a string of dna bases and returns a list with each base as a different
# element in the list.
def string_to_list(string):
    lis = []
    for i in range(len(string)):
        lis.append(string[i])
    return lis

# takes a seq dictionary and turns each seq string values into a list with each
# base as a different element and returns the dictionary with the list values.
def dict_values_to_list(d):
    new_d = {}
    for i in d.keys():
        string = d[i]
        l = string_to_list(string)
        new_d[i] = l
    return new_d

# takes a series and returns the value counts.
def value_counts(series):
    return series.value_counts()

# create a df with value counts for each base at each position
def profile_maker(df):
    # creates a dictionary to hold the counts of each base
    profile_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    # take the profile_dict and turns it into a pandas df.
    profile_df = pd.DataFrame.from_dict(profile_dict,orient='index').sort_index()
    # takes the df that has the different seq as the row ids and the bases in
    # the sequence as a value in each column.  Then apply each column to
    # value counts to find the number of each base at each position/column
    profile_df = df.apply(value_counts, axis=0).fillna(0)
    # for each column in df change values to integers
    for i in range(len(profile_df.columns.values)):
        profile_df[i] = profile_df[i].astype(int)
    # return value counts df
    return profile_df

# returns the max value in a series
def max_value_counts(series):
    return series.idxmax()

def common_ancestor(df):
    # create a df with value counts for each base at each position
    profile_df = profile_maker(df)
    # find the base with the max value in each position/column in the dataframe
    base_max_values = profile_df.apply(max_value_counts, axis=0)
    # change max values series to list.
    seq_list = base_max_values.tolist()
    # change seq_list to string
    seq = ''.join(seq_list)
    return seq

def consensus_profile(filename):
    # create dictionary of sequences from fatas file
    fasta_dict = make_indexed_sequences_dictionary(filename)
    # takes a seq dictionary and turns each seq string values into a list with
    # each base as a different element and returns the dictionary with the list
    # values.
    fasta_dict = dict_values_to_list(fasta_dict)
    #  creates a df from fasta sequence dictionary
    fasta_df = pd.DataFrame.from_dict(fasta_dict,orient='index').sort_index()
    # Creates a common ancestor sequence from fasta_df
    seq = common_ancestor(fasta_df)
    return seq
