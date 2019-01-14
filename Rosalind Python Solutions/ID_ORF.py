# http://rosalind.info/problems/orf/

# Given: A DNA string s of length at most 1 kbp in FASTA format.

# Return: Every distinct candidate protein string that can be translated from
# ORFs of s. Strings can be returned in any order.

import string

# return a complement string of dna
def complement_DNA(s):
    s.upper()
    # returns a translation table that maps each character in the
    # intabstring into the character at the same position in the outtab
    # string. Then this table is passed to the translate() function.
    trans_DNA = string.maketrans('ATCG', 'TAGC')
    sc = s.translate(trans_DNA)
    return sc

# return a reverse string
def reverse_string(s):
    return s[::-1]

# replaces T with U in a given string
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

# finds the start index and returns the sequence from the start seuqence
# to the end.
def translate_from_start(rnaseq):
    seq = translate(rnaseq)
    start_index = seq.find('M')
    if (start_index >= 0) and (seq[start_index] == 'M'):
        return seq[start_index:]
    else:
        return False

# for each reading frame find a protein if it has a starting codon
def translate_3_reading_frames(rna):
    protein_list = []
    for i in range(3):
        aa = translate_from_start(rna[i:])
        if aa:
            protein_list.append(aa)
    return protein_list

def open_reading_frames(dna):
    # return a complement string of dna
    cdna = complement_DNA(dna)
    # replaces T with U in a given string
    rna = transcribe_DNA_to_RNA(dna)
    crna = transcribe_DNA_to_RNA(cdna)
    # return a reverse string
    reverse_crna = reverse_string(crna)
    # for each reading frame find a protein if it has a starting codon
    aa_list = translate_3_reading_frames(rna)
    raa_list = translate_3_reading_frames(reverse_crna)
    # returns the proteins from sequence and reverse sequence
    return aa_list + raa_list
