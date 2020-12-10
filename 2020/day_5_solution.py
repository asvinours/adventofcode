#!python

import re

with open('day_5_input.txt') as f:
    lines = f.read().splitlines()

print("part 1")

rows = range(128)
columns = range(8)

def find_half(rng, code):
    half = len(rng)//2
    lowerhlf = rng[:half]
    upperhlf = rng[half:]

    if code == 'F' or code == 'L':
        return lowerhlf
    return upperhlf

max_seat_id = 0
seats = []
for l in lines:
    rid = l[:7]
    cid = l[7:]
    search_in = rows
    for r in rid:
        search_in = find_half(search_in, r)
    row = search_in[0]

    search_in = columns
    for c in cid:
        search_in = find_half(search_in, c)
    column = search_in[0]

    seat_id = int(row) * 8 + int(column)
    seats.append(seat_id)
    max_seat_id = max(max_seat_id, seat_id)

print(max_seat_id)

print("part 2")

seats.sort()
for i in range(len(seats)):
    if i == 0:
        continue
    if i == len(seats)-1:
        continue
    ns = seats[i+1]
    s = seats[i]

    if ns - s > 1:
        print(ns, s)
