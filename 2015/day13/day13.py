#!/usr/bin/env python

from itertools import permutations
from sys import maxsize
import fileinput

def add_family_member(d, l):
    if len(l.split()) != 11:
        return
    (key, sign, value, item) = [ l.split()[0], l.split()[2], int(l.split()[3]), l.split()[10][:-1] ] 
    if sign == "lose":
        value = ~value + 1
    if d.has_key(key):
        d[key][item] = value
    else:
        d[key] = { item: value }

def happiest_scenario(d):
    scenarios = []
    max_happiness_score = 0
    for scenario in permutations(d):
        happiness_score = 0
        for family_member in scenario:
            individual_score = score(family_member, scenario, d)
            happiness_score = happiness_score + individual_score
        if happiness_score > max_happiness_score:
            max_happiness_score = happiness_score
            happiest_scenario = scenario
    print max_happiness_score, happiest_scenario
    return scenarios

def score(item, scenario, data):
    scores = data[item]
    index = scenario.index(item)
    return data[item][scenario[(index + 1) % len(scenario)]] + data[item][scenario[(index - 1) % len(scenario)]]

if __name__ == '__main__':
    data = {} 
    for n, line in enumerate(fileinput.input()):
        add_family_member(data, line)
    happiest_scenario(data)
    #shortest(data)
    #longest(data)
