# http://rosalind.info/problems/fibd/

# Given: Positive integers n≤100 and m≤20.

# Return: The total number of pairs of rabbits that will remain after the n-th
# month if all rabbits live for m months.

def mortal_fibonacci(n, m):
    # Make an array of alive rabbits at length months lived (m) and set the
    # the first alive rabbit to 1 to start population
    ages = [0]*m
    ages[0] = 1
    # for each n-th month in base 0
    for i in range(n-1):
        # one rabbit pair being born for each mature rabbit pair
        born = sum(ages[1:])
        # rabbits that will be alive next month
        alive = ages[:-1]
        # dying rabbits
        dying = ages[-1]
        # array of alive rabbits
        ages = [born] + alive
    # return sum of all alive rabbits
    return sum(ages)
