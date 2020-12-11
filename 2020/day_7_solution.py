#!python3

import re

print("part 1")
rules = open('day_7_input.txt').read().strip().split('\n')

def find_match(rules, pattern):
    return [rule for rule in rules if re.search(r' contain .+? '+pattern+' bag', rule)]

next_elems = ['shiny gold']
found = set()
while len(next_elems) > 0:
    elem = next_elems.pop(0)
    if elem != 'shiny gold':
        found.add(elem)
    csg = find_match(rules, elem)
    pps = [re.search(r'^(.+?) bags contain', rule).group(1) for rule in csg]
    next_elems.extend(list(set(pps)))

print(len(found))

print("part 2")

def count_bags(colors, color):
    inside = colors[color]
    if len(inside) < 1:
        return 1
    c = 1
    for i in inside:
        rec = count_bags(colors, i[1])
        c = c + (int(i[0]) * rec)
    return c

colors = {}
for rule in rules:
    color, rest = rule.split('bags contain')
    colors[color.strip()] = []
    if 'no other bag' in rest:
        continue
    ins = rest.split(',')
    for bg in ins:
        m = re.search(r'([0-9]+) ([a-z\s]+) bags?', bg)
        colors[color.strip()].append((m.group(1), m.group(2)))

print(count_bags(colors, 'shiny gold')-1)
