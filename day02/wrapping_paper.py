#!/usr/bin/env python

import fileinput

def area_required(dimensions):
    l, w, h = get_dimensions(dimensions)
    a = [ l*w, l*h, w*h ]
    return 2*sum(a) + min(a)

def length_required(dimensions):
    l, w, h = get_dimensions(dimensions)
    return l*w*h + 2*(sum([l, w, h]) - max(l, w, h)) 

def get_dimensions(s):
    try:
        return map(int, s.split('x'))
    except ValueError:
        return [0, 0, 0]
    
if __name__ == '__main__':
    area = 0
    length = 0
    for line in fileinput.input():
        area += area_required(line)
        length += length_required(line)
    print 'Wrapping paper required: %i' % area
    print 'Ribbon required: %i' % length
