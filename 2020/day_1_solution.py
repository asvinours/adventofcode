#!python

with open('day_1_input.txt') as f:
    lines = f.read().splitlines()

def sum(*args):
    return reduce((lambda x, y: x + y), args)

expenses = list(map(int, lines))

for i in range(len(expenses)-1):
    for j in range(len(expenses)-1):
        if i == j:
            continue

        for k in range(len(expenses)-1):
            if i == k or k == j:
                continue

            sumsum = sum(expenses[i], expenses[j], expenses[k])
            if sumsum == 2020:
                print(expenses[i] * expenses[j] * expenses[k])
                exit(0)
