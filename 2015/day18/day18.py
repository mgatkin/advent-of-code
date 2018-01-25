#!/usr/bin/env python

import argparse
import fileinput

def build_map(d):
    data = []
    for line in d:
        data = data + [[ 1 if c == '#' else 0 for c in line ]]
    return data

def count_neighbors(d, coords): 
    (row, col) = coords
    neighbors_on = 0
    for c_row in xrange(3):
        for c_col in xrange(3):
            if c_row is not 1 or c_col is not 1:
                try:
                    neighbors_on = neighbors_on + is_neighbor_on(d, (row + c_row - 1, col + c_col - 1))
                except TypeError:
                    print 'neighbors_on:', neighbors_on, type(neighbors_on)
                    print 'row:', row, type(row)
                    print 'col:', col, type(col)
                    print 'c_row:', c_row, type(c_row)
                    print 'c_col:', c_col, type(c_col)
    return neighbors_on

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

def next_state(d):
    new_d = []
    for row, row_data in enumerate(d):
        new_d = new_d + [[]]
        for col in xrange(len(row_data)):
            neighbors = count_neighbors(d, (row, col))
            if d[row][col] is 1:
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', default='1', help='Number of iterations')
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    args = parser.parse_args()

    data = []
    count = int(args.count)
    for line in fileinput.input(files=args.files):
        data = data + [ line.strip() ]
    data = build_map(data)
    for n in xrange(count):
        data = next_state(data)
    count = count_lights_on(data)
    if count == 1:
        print '1 light is on'
    else:
        print count, 'lights are on'

