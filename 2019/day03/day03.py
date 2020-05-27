#!/usr/bin/env python

import fileinput
from sys import maxint


def part1(data):
    wire_directions = [ data[0].split(','), data[1].split(',') ]
    wires = [ [ (0, 0) ], [ (0, 0) ] ]
    for w, wire in enumerate(wires):
        print 'Tracing wire', w
        current_pos = wires[w][len(wires[w]) - 1]
        for wire_direction in wire_directions[w]:
            direction = wire_direction[0]
            length = int(wire_direction[1:])
            for i in xrange(length):
                next_pos = find_next_position(current_pos, direction)
                wires[w].append(next_pos)
                current_pos = next_pos
    intersections = []
    print 'Finding intersections...'
    length = len(wires[0][1:])
    for i, w in enumerate(wires[0][1:]):
        if i % 100 == 0:
            print 'Checking', i, 'of', length
        if w in wires[1][1:]:
            intersections.append(w)
    #for s in wires[0][1:]:
    #    for d in wires[1][1:]:
    #        if s == d:
    #            intersections.append(s)
    shortest_distance = maxint
    closest_point = None
    for i in intersections:
        distance = abs(i[0]) + abs(i[1])
        if distance < shortest_distance:
            closest_point = i
            shortest_distance = distance
    if closest_point is not None:
        print closest_point, shortest_distance
    else:
        print 'No intersection detected.'


def find_next_position(position, direction):
    if direction == 'R':
        adder = (1, 0)
    elif direction == 'U':
        adder = (0, 1)
    elif direction == 'L':
        adder = (-1, 0)
    elif direction == 'D':
        adder = (0, -1)
    else:
        adder = (0, 0)
    return add_tuple(position, adder)


def add_tuple(a, b):
    if len(a) == len(b) == 2:
        return (a[0] + b[0], a[1] + b[1])


if __name__ == '__main__':
    file_input = fileinput.input()
    lines = [ file_input.readline().strip(), file_input.readline().strip() ]
    part1(lines)

