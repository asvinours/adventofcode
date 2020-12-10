#!python

import re

with open('day_4_input.txt') as f:
    lines = f.read().splitlines()

print("part 1")

valid = 0
required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passeport = []
for l in lines:
    if len(l) == 0:
        intersect = list(set(passeport) & set(required_keys))
        if len(intersect) == len(required_keys):
            valid = valid + 1

        passeport = []
    else:
        parts = l.split(' ')
        for p in parts:
            key, value = p.split(':')
            passeport.append(key)

print(valid)

print("part 2")

def valid_passeport(passeport):
    pp_keys = passeport.keys()
    intersect = list(set(pp_keys) & set(required_keys))
    if len(intersect) != len(required_keys):
        return False

    if int(passeport['byr']) < 1920 or int(passeport['byr']) > 2002:
        return False

    if int(passeport['iyr']) < 2010 or int(passeport['iyr']) > 2020:
        return False

    if int(passeport['eyr']) < 2020 or int(passeport['eyr']) > 2030:
        return False

    if 'cm' in passeport['hgt']:
        hgt = passeport['hgt'].replace('cm', '')
        if int(hgt) < 150 or int(hgt) > 193:
            return False
    elif 'in' in passeport['hgt']:
        hgt = passeport['hgt'].replace('in', '')
        if int(hgt) < 59 or int(hgt) > 76:
            return False
    else:
        return False

    m = re.match(r'\#[a-f0-9]{6}', passeport['hcl'])
    if not m:
        return False

    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if passeport['ecl'] not in ecls:
        return False

    m = re.match(r'[0-9]{9}', passeport['pid'])
    if not m or len(passeport['pid']) > 9:
        return False

    return True

valid = 0
required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passeport = {}
for l in lines:
    if len(l) == 0:
        if valid_passeport(passeport):
            valid = valid + 1

        passeport = {}
    else:
        parts = l.split(' ')
        for p in parts:
            key, value = p.split(':')
            passeport[key] = value

print(valid)
