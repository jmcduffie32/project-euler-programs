import itertools
digits = [0,1,2,3,4,5,6,7,8,9]

possibilities = itertools.permutations(digits)
print list(possibilities)[999999]
#possibilites = sorted(possibilities)


