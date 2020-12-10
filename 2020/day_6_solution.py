#!python3

print("part 1")
groups = open('day_6_input.txt').read().strip().split('\n\n')

tot = 0
for g in groups:
    count = len(set(g.replace('\n', '')))
    tot = tot + count

print(tot)

print("part 2")

tot = 0
for g in groups:
    pps = g.split('\n')
    res = None
    for p in pps:
        if res is None:
            res = p
        else:
            res = set(res).intersection(p)
    tot = tot + len(res)
print(tot)
