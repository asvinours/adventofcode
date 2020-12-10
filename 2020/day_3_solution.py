#!python

import re

with open('day_3_input.txt') as f:
    lines = f.read().splitlines()

def count_trees(lines, right, down):
    trees = 0
    cursor = 0
    width = len(lines[0])
    for i in range(len(lines)):
        if i % down != 0:
            continue
        l = lines[i]
        space = l[cursor]
        if space == '#':
            trees = trees + 1

        if cursor+right >= width:
            cursor = abs(width - (cursor+right))
        else:
            cursor = cursor+right

    return trees

print("part 1")
print(count_trees(lines, 3, 1))


print("part 2")
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
product = 1
for slope in slopes:
    treecount = count_trees(lines, slope[0], slope[1])
    print(treecount)
    product = product * treecount

print(product)
