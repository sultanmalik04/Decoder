# combinations function takes one iterable and r as input and return object list of tuples
# which contains all possible combinations of length r
# so here logic is the player plays 2 times with the single opponent
# so we will multiply the number of combinations by 2.

from itertools import combinations
n = int(input())
print(2*len(list(combinations(range(n), 2))))