#!/usr/bin/env python

import fileinput
from sys import maxint
from time import time


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
    w = 1
    wire = wires[w]
    intersections = []
    print 'Finding intersections...'
    wire_length = len(wires[0][1:])
    current_pos = wires[w][0]
    position = 0
    for wire_direction in wire_directions[w]:
        direction = wire_direction[0]
        length = int(wire_direction[1:])
        for i in xrange(length):
            next_pos = find_next_position(current_pos, direction)
            wires[w].append(next_pos)
            current_pos = next_pos
            if position % 100 == 0:
                print 'Checking', position, 'of', wire_length
            if current_pos in wires[0][1:]:
                intersections.append(current_pos)
            position = position + 1
    #print wires, intersections
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
    return wires, intersections


def part1_first_algorithm(data):
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
    return wires, intersections


def part1_second_algorithm(data):
    wire_directions = [ data[0].split(','), data[1].split(',') ]
    wires = [ [ (0, 0) ], [ (0, 0) ] ]
    w = 0
    wire = wires[w]
    print 'Tracing wire', w
    current_pos = wires[w][0]
    for wire_direction in wire_directions[w]:
        direction = wire_direction[0]
        length = int(wire_direction[1:])
        for i in xrange(length):
            next_pos = find_next_position(current_pos, direction)
            wires[w].append(next_pos)
            current_pos = next_pos
    w = 1
    wire = wires[w]
    intersections = []
    print 'Tracing wire', w
    current_pos = wires[w][0]
    for wire_direction in wire_directions[w]:
        direction = wire_direction[0]
        length = int(wire_direction[1:])
        for i in xrange(length):
            next_pos = find_next_position(current_pos, direction)
            wires[w].append(next_pos)
            current_pos = next_pos
            if current_pos in wires[0][1:]:
                intersections.append(current_pos)
    #print wires, intersections
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
    return wires, intersections


def part2(wires, intersections):
    #print 'wires =', wires
    #print 'intersections =', intersections
    min_delay = maxint
    for i in intersections:
        delay = wires[0].index(i) + wires[1].index(i)
        min_delay = delay if delay < min_delay else min_delay
    print min_delay


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


def processing_time(f, arg):
    start_time = time()
    result = f(arg)
    print 'Processing', f.__name__, 'took', time() - start_time, 'seconds.'
    return result


if __name__ == '__main__':
    file_input = fileinput.input()
    lines = [ file_input.readline().strip(), file_input.readline().strip() ]
    processing_time(part1_first_algorithm, lines)
    processing_time(part1_second_algorithm, lines)
    wires, intersections = processing_time(part1, lines)
    part2(wires, intersections)

