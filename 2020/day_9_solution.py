#!python3

from collections import deque
from itertools import combinations

print("part 1")
digits = open('day_9_input.txt').read().strip().split('\n')
size = 25

b = []
l = deque(maxlen=size)
invalid = None
for d in digits:
    if len(l) == size:
        valid = next(iter([True for p in combinations(l, 2) if sum(p) == int(d)]), False)
        if not valid:
            invalid = int(d)
            break
      
    b.append(int(d))
    l.append(int(d))

print(invalid)

print("part 2")

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

for i in range(2, len(b)):
    for j in range(len(b)):
        for c in chunks(b[j:], i):
            if sum(c) == invalid:
                print(c)
                u = sorted(c)
                print(sum([u[0], u[-1]]))
                exit(0)
