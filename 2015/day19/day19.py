#!/usr/bin/env python

import argparse
import fileinput

def build_map(d, stuck = False):
    data = []
    for line in d:
        data = data + [[ 1 if c == '#' else 0 for c in line ]]
    if stuck:
        end = len(data[0]) - 1
        data[0][0] = 1
        data[0][end] = 1
        data[end][0] = 1
        data[end][end] = 1
    return data

def count_neighbors(d, coords): 
    (row, col) = coords
    neighbors_on = 0
    for c_row in xrange(3):
        for c_col in xrange(3):
            if c_row is not 1 or c_col is not 1:
                neighbors_on = neighbors_on + is_neighbor_on(d, (row + c_row - 1, col + c_col - 1))
    return neighbors_on

def is_a_corner(coords, length):
    (row, col) = coords
    if (row is 0 and col is 0) or \
            (row is 0 and col is length - 1) or \
            (row is length - 1 and col is 0) or \
            (row is length - 1 and col is length - 1):
        return True
    else:
        return False

def is_neighbor_on(d, coords):
    (row, col) = coords
    length = len(d[0])
    if row < 0 or col < 0 or row >= length or col >= length:
        return 0
    else:
        return d[row][col]

def count_lights_on(d):
    total = 0
    for row in d:
        total = total + sum(row)
    return total

def next_state(d, stuck = False):
    new_d = []
    for row, row_data in enumerate(d):
        new_d = new_d + [[]]
        for col in xrange(len(row_data)):
            neighbors = count_neighbors(d, (row, col))
            if stuck and is_a_corner((row, col), len(row_data)):
                new_d[row] = new_d[row] + [ 1 ]
            elif d[row][col] is 1:
                if neighbors is 2 or neighbors is 3:
                    new_d[row] = new_d[row] + [ 1 ]
                else:
                    new_d[row] = new_d[row] + [ 0 ]
            else:
                if neighbors is 3:
                    new_d[row] = new_d[row] + [ 1 ]
                else:
                    new_d[row] = new_d[row] + [ 0 ]
    return new_d

def get_state(d):
    data = []
    for row in d:
        data = data + [ ''.join([ '#' if c else '.' for c in row ]) ]
    return data

def print_state(d):
    for row in d:
        print ''.join([ '#' if c else '.' for c in row ])

def unique_combinations(e, s):
    return

def process_molecules(s, m):
    c = []
    for e in m:
        unique_combinations(e, s)
    return c

def build_tables(d):
    data = {}
    molecules = []
    for i in d:
        a = i.split()
        if len(a) == 3 and a[1] == '=>':
            if a[0] not in data:
                data[a[0]] = []
            data[a[0]] = data[a[0]] + [ a[2] ]
        elif len(a) == 1:
            molecules = molecules + a
    return data, molecules

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('-c', '--count', default='1', help='Number of iterations')
    #parser.add_argument('-s', '--stuck', action='store_true', help='Corners are stuck on')
    parser.add_argument('-v', '--verbose', action='count', help='Verbose output')
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    args = parser.parse_args()

    #count = int(args.count)
    #stuck = args.stuck
    verbose = args.verbose

    data = []
    for line in fileinput.input(files=args.files):
        data = data + [ line.strip() ]
    substitutions, molecules = build_tables(data)
    if verbose > 0:
        print substitutions, molecules
'''
    for n in xrange(count):
        data = next_state(data, stuck)
        if verbose:
            print_state(data)
    count = count_lights_on(data)
    if count == 1:
        print '1 light is on'
    else:
        print count, 'lights are on'
'''
