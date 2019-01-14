# http://rosalind.info/problems/prot/

# Given: An RNA string s corresponding to a strand of mRNA (of length at most
# 10 kbp).

# Return: The protein string encoded by s.

# returns aa from RNA_codon_table
def translate_RNA_codon(codon):
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

    return RNA_codon_table[codon]

# Translate rnaseq into amino acid symbols
def aa_generator(rnaseq):
    # Return a generator object that produces an amino acid by translating
    # three characters of rnaseq at a time
    return (translate_RNA_codon(rnaseq[n:n+3]) for n in range(0, len(rnaseq), 3))

# translates an rna sequence until stop codon is found and returns aa
# sequence
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
