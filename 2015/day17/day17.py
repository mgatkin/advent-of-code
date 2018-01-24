#!/usr/bin/env python

from sys import maxint
from itertools import combinations
import fileinput

def number_of_combinations(data, total): 
    number_of_valid_combinations = 0
    valid_combinations = []
    for n, i in enumerate(data):
        for c in combinations(data, n + 1):
            if sum(c) == total:
                number_of_valid_combinations = number_of_valid_combinations + 1
                valid_combinations = valid_combinations + [ c ]
    return number_of_valid_combinations, valid_combinations

def minimum_containers(data):
    minimum_number_of_containers = maxint
    for n in data:
        if len(n) < minimum_number_of_containers:
            minimum_number_of_containers = len(n)
    number_of_combinations = 0
    for n in data:
        if len(n) == minimum_number_of_containers:
            number_of_combinations = number_of_combinations + 1
    return minimum_number_of_containers, number_of_combinations

if __name__ == '__main__':
    data = []
    for line in fileinput.input():
        data = data + [ int(line) ]
    count = [ 25, 150 ]
    for n in count:
        (number_of_valid_combinations, valid_combinations) = number_of_combinations(data, n)
        print 'There are', number_of_valid_combinations,
        print 'combinations of containers for', n, 'liters of eggnog.'
        (number_of_minimum_containers, number_of_minimum_container_combinations) = \
                minimum_containers(valid_combinations)
        print 'There are', number_of_minimum_container_combinations,
        print 'combinations that use the minimum of', number_of_minimum_containers, 'containers.'


