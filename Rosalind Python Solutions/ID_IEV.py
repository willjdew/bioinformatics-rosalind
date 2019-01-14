# http://rosalind.info/problems/iev/

# Given: Six nonnegative integers, each of which does not exceed 20,000. The
# integers correspond to the number of couples in a population possessing each
# genotype pairing for a given factor. In order, the six given integers
# represent the number of couples having the following genotypes:

# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa

# Return: The expected number of offspring displaying the dominant phenotype in
# the next generation, under the assumption that every couple has exactly two
# offspring.

# Generates a dictionary with genotypes as keys and number of genotypes as
# values
def make_geno_dict(num_couples):
    # declare new dict geno and list of genotype pairs
    geno_dict = {}
    geno = ["AA-AA", "AA-Aa", "AA-aa", "Aa-Aa", "Aa-aa", "aa-aa"]

    # for each genotype pair add it and the number of couples to the geno dict
    for idx, g in enumerate(geno):
        geno_dict[g] = num_couples[idx]

    return geno_dict

# Given a list of six numbers returns the expected number of dominant
# phenotypes
def cal_exp_offspring(num_couples):
    # make dict from num_couples
    geno = make_geno_dict(num_couples)

    # Probabilty of pairs producing a dominate phenotype
    multiplier = {"AA-AA": 1.0,
                  "AA-Aa": 1.0,
                  "AA-aa": 1.0,
                  "Aa-Aa": 0.75,
                  "Aa-aa": 0.50,
                  "aa-aa": 0.0}
    # Each couple has exactly 2 offspring times the number of genotype pairing
    # times the probability of getting a domominat phenotype in the next
    # generation plus the previous phenotype pairs' probability
    exp = 0
    for x in geno.keys():
        exp = exp + 2 * geno[x] * multiplier[x]
    return exp
