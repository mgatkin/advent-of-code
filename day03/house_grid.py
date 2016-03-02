#!/usr/bin/env python

import fileinput

def count_presents(directions):
    x = 0
    y = 0
    houses_delivered = 1
    grid = { (0, 0) }
    for move in directions:
        x, y = next_house([x, y], move)
        grid.add((x, y))
    return len(grid)

def next_house(coords, direction):
    x, y = coords
    if direction == '<':
        x = x - 1
    if direction == '^':
        y = y - 1
    if direction == '>':
        x = x + 1
    if direction == 'v':
        y = y + 1
    return x, y

if __name__ == '__main__':
    for line in fileinput.input():
        print 'Delivered to %i houses' % count_presents(line)

