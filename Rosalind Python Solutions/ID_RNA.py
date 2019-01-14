# http://rosalind.info/problems/rna/

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

def transcribe_DNA_to_RNA(t):
    t.upper()
    t = t.replace('T', 'U')
    return t
