#!/usr/bin/env python

import fileinput

def find_aunt(d, calibrated = False): 
    AuntSue = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
        }
    PossibleAunts = []
    for aunt in d:
        IsExcluded = False
        for attribute in d[aunt]:
            if attribute in AuntSue:
                print attribute
                if calibrated:
                    if attribute is 'cats' or attribute is 'trees':
                        if AuntSue[attribute] <= int(d[aunt][attribute]):
                            IsExcluded = True
                    elif attribute is 'pomeranians' or attribute is 'goldfish':
                        if AuntSue[attribute] >= int(d[aunt][attribute]):
                            IsExcluded = True
                    elif AuntSue[attribute] != int(d[aunt][attribute]):
                        IsExcluded = True
                else:
                    if AuntSue[attribute] != int(d[aunt][attribute]):
                        IsExcluded = True
        if not IsExcluded:
            return aunt
    return None

def add_aunt(d, l):
    s = l.split()
    if len(s) != 8:
        return
    d[s[1][:-1]] = {}
    d[s[1][:-1]][s[2][:-1]] = s[3][:-1]
    d[s[1][:-1]][s[4][:-1]] = s[5][:-1]
    d[s[1][:-1]][s[6][:-1]] = s[7]

if __name__ == '__main__':
    data = {}
    for n, line in enumerate(fileinput.input()):
        add_aunt(data, line)
    print 'Aunt', find_aunt(data)
    print 'Aunt', find_aunt(data, calibrated = True)

