# http://rosalind.info/problems/splc/

# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
# of s acting as introns. All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons
# of s. (Note: Only one solution will exist for the dataset provided.)

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

def transcribe_DNA_to_RNA(t):
    t.upper()
    t = t.replace('T', 'U')
    return t

# Translating RNA into Protien
RNA_codon_table = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
}

def translate_RNA_codon(codon):
    return RNA_codon_table[codon]

def aa_generator(rnaseq):
    # Return a generator object that produces an amino acid by translating
    # three characters of rnaseq at a time
    return (translate_RNA_codon(rnaseq[n:n+3]) for n in range(0, len(rnaseq), 3))

def translate(rnaseq):
    rnaseq = rnaseq.upper()
    # Translate rnaseq into amino acid symbols
    gen = aa_generator(rnaseq)
    seq = ''
    # Sets the first amino acid as 'aa'
    aa = next(gen, None)
    # While aa is true
    while aa:
        # If aa is a stop codon retrun sequence else add aa to seq
        if aa == 'Stop':
            return seq
        else:
            seq += aa
            aa = next(gen, None)
    return seq

# Find the key with the longest seq
def find_max_len_seq_key(d):
    max_len = 0
    max_key = ''
    for key in d.keys():
        seq_len = len(d[key])
        if seq_len > max_len:
            max_len = seq_len
            max_key = key
    return max_key

# replace intron in string
def remove_introns(seq, intron):
    return seq.replace(intron, '')

def rna_splicing(filename):
    # Make dna seq dict from fasta file
    d = make_indexed_sequences_dictionary(filename)
    # Find the key with the longest seq
    max_key = find_max_len_seq_key(d)

    # copy seq and delete key
    seq = d[max_key]
    d.pop(max_key, None)

    # for each intron remove it from seq
    for v in d.values():
        seq = remove_introns(seq, v)

    # transcribe dna to rna and translate it to a protein
    seq = transcribe_DNA_to_RNA(seq)
    return translate(seq)
