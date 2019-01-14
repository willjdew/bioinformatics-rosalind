# http://rosalind.info/problems/iprb/

# Given: Three positive integers k, m, and n, representing a population
# containing k+m+n organisms: k individuals are homozygous dominant for a
# factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will
# produce an individual possessing a dominant allele (and thus displaying the
# dominant phenotype). Assume that any two organisms can mate.

import scipy.special

def dominate_allele(k, m, n):
    # Calculate total number of organisms in the population:
    total_pop = k + m + n
    # Calculate the number of combos that could be made (valid or not):
    total_comb = scipy.special.comb(total_pop, 2)
    # Calculate the number of combos that have a dominant allele therefore are
    # valid:
    valid_comb = scipy.special.comb(k, 2) + k*m + k*n + 0.75*scipy.special.comb(m, 2) + 0.5*m*n + 0.0
    # Calculate the probability of valid combos
    prob = valid_comb / total_comb
    return prob   
