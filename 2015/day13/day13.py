#!/usr/bin/env python

from itertools import permutations
from sys import maxsize
import fileinput

def add_relationship(d, l):
    if len(l.split()) != 11:
        return
    (key, sign, value, item) = [ l.split()[0], l.split()[2], int(l.split()[3]), l.split()[10][:-1] ] 
    if sign == "lose":
        value = ~value + 1
    if d.has_key(key):
        d[key][item] = value
    else:
        d[key] = { item: value }

def add_self(d):
    copy_of_d = dict(d)
    for family_member in copy_of_d:
        add_relationship(d, 'SELF would gain 0 happiness units by sitting next to ' + family_member + '.')
        add_relationship(d, family_member + ' would gain 0 happiness units by sitting next to SELF.')

def find_happiest_scenario(d):
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
    return max_happiness_score, happiest_scenario

def score(item, scenario, data):
    scores = data[item]
    index = scenario.index(item)
    return data[item][scenario[(index + 1) % len(scenario)]] + data[item][scenario[(index - 1) % len(scenario)]]

if __name__ == '__main__':
    data = {} 
    for n, line in enumerate(fileinput.input()):
        add_relationship(data, line)
    first_max_happiness_score, first_happiest_scenario = find_happiest_scenario(data)
    print 'Highest happiness score is', first_max_happiness_score, '=>',
    for n in first_happiest_scenario:
        print n,
    print
    add_self(data)
    second_max_happiness_score, second_happiest_scenario = find_happiest_scenario(data)
    print 'Highest happiness score after adding myself is', second_max_happiness_score, '=>',
    for n in second_happiest_scenario:
        print n,
    print
