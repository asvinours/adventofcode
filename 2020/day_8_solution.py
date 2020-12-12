#!python3

print("part 1")
lines = open('day_8_input.txt').read().strip().split('\n')

def find_wally(lns):
    acc = 0
    cursor = 0
    visited = set()
    max_l = len(lns)-1
    while cursor >= 0 and cursor <= max_l:
        l = lns[cursor]
        if cursor in visited:
            return (False, acc)

        p = l.split(' ')
        visited.add(cursor)
        if p[0] == 'nop':
            acc = acc
        elif p[0] == 'acc':
            acc = acc + int(p[1])
        elif p[0] == 'jmp':
            cursor = cursor + int(p[1])
            continue
        cursor = cursor + 1
    return (True, acc)

r, accg = find_wally(lines)
print(accg)

print("part 2")

for i in range(len(lines)):
    l = lines[i]
    p = l.split(' ')
    if p[0] == 'nop' or p[0] == 'jmp':
        cpl = lines[:]
        if p[0] == 'nop':
            cpl[i] = lines[i].replace('nop', 'jmp')
        else:
            cpl[i] = lines[i].replace('jmp', 'nop')
        r, acc = find_wally(cpl)
        if r:
            print(acc)
            break

