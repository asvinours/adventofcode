#!python

from itertools import combinations

with open('day_1_input.txt') as f:
    lines = f.read().splitlines()

def sum(*args):
    return reduce((lambda x, y: x + y), args)

def product(*args):
    return reduce((lambda x, y: x * y), args)

expenses = list(map(int, lines))
combs = combinations(expenses, 3)
for c in combs:
    if sum(*c) == 2020:
        print(product(*c))
        break

