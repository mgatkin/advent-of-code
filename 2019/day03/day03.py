#!/usr/bin/env python

import fileinput

def part1(data):
    wire_directions = [ data[0].strip().split(','), data[1].strip().split(',') ]
    wires = [ [ (0, 0) ], [ (0, 0) ] ]
    for wire in wires:
        for d in wire_directions:
            current_pos = wire[len(wire) - 1]
            direction = d[0]
            length = int(d[0:])
            for i in enumerate(length):
                next_pos = find_next_position(current_pos, direction, length)
                wire.append(next_pos)
            current_pos = next_pos

    for d in wire2:
        print(d)

def find_next_position(position, direction, length):
    if direction == 'U':
        adder = (0, -1)
    elif direction == 'D':
        adder = (0, 1)
    elif direction == 'L':
        adder = (-1, 0)
    elif direction == 'R':
        adder = (1, 0)
    else:
        adder = (0, 0)
    return position

def function2(d): 
    return d

if __name__ == '__main__':
    file_input = fileinput.input()
    part1(file_input)
    for n, line in enumerate(file_input):
        print 'Executing function1 on line', (n + 1), 'returned', function1(line)
        print 'Executing function2 on line', (n + 1), 'returned', function2(line)
