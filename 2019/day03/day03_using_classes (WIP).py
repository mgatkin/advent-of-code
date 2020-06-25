#!/usr/bin/env python

import fileinput


class VerticalSegment:
    def __init__(self, x, y1, y2):
        self.X = x
        self.Y1 = y1
        self.Y2 = y2


    def __eq__(self, v):
        if type(v) is not type(self):
            raise Exception('InvalidType')
        else:
            return v.X == self.X and v.Y1 == self.Y1 and v.Y2 == self.Y2
    

    def __ne__(self, v):
        if type(v) is not type(self):
            raise Exception('InvalidType')
        else:
            return v.X != self.X or v.Y1 != self.Y1 or v.Y2 != self.Y2
    

    def __str__(self):
        return str('(%d, %d, %d)\n' % (self.X, self.Y1, self.Y2))
        
        
class HorizontalSegment:
    def __init__(self, y, x1, x2):
        self.Y = y
        self.X1 = x1
        self.X2 = x2


    def __eq__(self, h):
        if type(v) is not type(self):
            raise Exception('InvalidType')
        else:
            return h.Y == self.Y and h.X1 == self.X1 and h.X2 == self.X2
    

    def __ne__(self, y, x1, x2):
        if type(v) is not type(self):
            raise Exception('InvalidType')
        else:
            return h.Y != self.Y or h.X1 != self.X1 or h.X2 != self.X2
    

    def __str__(self):
        return str('(%d, %d, %d)\n' % (self.Y, self.X1, self.X2))

        
class Wire:
    def __init__(self):
        self.Verticals = []
        self.Horizontals = []


    def AddVertical(self, segment):
        self.Verticals.append(segment)


    def AddHorizontal(self, segment):
        self.Horizontals.append(segment)


def ProcessWire(directions):
    coord = [0, 0]
    wire = Wire()
    for d in directions:
        if d[0] == 'U' or d[0] == 'D':
            length = int(d[1:])
            wire.AddVertical(VerticalSegment(coord[0], coord[1], coord[1] + length))
            coord[1] = coord[1] + length
        elif d[0] == 'L' or d[0] == 'R':
            length = int(d[1:])
            wire.AddHorizontal(HorizontalSegment(coord[1], coord[0], coord[0] + int(d[1:])))
            coord[0] = coord[0] + length
        else:
            print('ERROR: Uknown direction - %s (%d))\n' % (d[0], d[0]))
            return None
    return wire


def part1():
    return


def part2():
    return


if __name__ == '__main__':
    file_input = fileinput.input()
    lines = [ file_input.readline().strip().split(','), file_input.readline().strip().split(',') ]
    wires = []
    for line in lines:
        wires.append(ProcessWire(line))
    for wire in wires:
        for h in wire.Horizontals:
            print(h)
        for v in wire.Verticals:
            print(v)
            
v = []
v.append(VerticalSegment(1, 2, 3))
v.append(VerticalSegment(1, 2, 3))
v.append(VerticalSegment(1, 2, 5))
h = []
h.append(HorizontalSegment(1, 2, 3))
h.append(HorizontalSegment(1, 2, 4))
h.append(HorizontalSegment(1, 2, 5))
print(v[0] == v[1])
print(v[0] == v[2])

