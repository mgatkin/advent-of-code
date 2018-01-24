#!/usr/bin/env python

from itertools import combinations
import fileinput

def number_of_combinations(data, total): 
    number_of_combinations = 0
    for n, i in enumerate(data):
        for c in combinations(data, n + 1):
            if sum(c) == total:
                number_of_combinations = number_of_combinations + 1
    return number_of_combinations 

if __name__ == '__main__':
    data = []
    for line in fileinput.input():
        data = data + [ int(line) ]
    count = [ 25, 150 ]
    for n in count:
        print 'There are', number_of_combinations(data, n), 'combinations of containers for', n, 'liters of eggnog.'


