#!python

import re

with open('day_2_input.txt') as f:
    lines = f.read().splitlines()

print("part 1")

valid = 0
for l in lines:
    parts = l.split(" ")
    min_oc, max_oc = parts[0].split("-")
    letter = parts[1][0]
    password = parts[-1]

    c = password.count(letter)
    if c >= int(min_oc) and c <= int(max_oc):
        valid = valid+1

print(valid)

print("part 2")

valid = 0
for l in lines:
    parts = l.split(" ")
    min_oc, max_oc = parts[0].split("-")
    letter = parts[1][0]
    password = parts[-1]

    blurp = "{}{}".format(password[int(min_oc)-1], password[int(max_oc)-1])
    if blurp.count(letter) == 1:
        valid = valid+1

print(valid)
