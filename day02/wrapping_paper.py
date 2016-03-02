#!/usr/bin/env python

import fileinput

def area_required(s):
    try:
        l, w, h = get_dimensions(s)
        a = [ l*w, l*h, w*h ]
        return 2*sum(a) + min(a)
    except TypeError:
        return 0

def length_required(s):
    try:
        l, w, h = get_dimensions(s)
        return l*w*h + 2*(sum([l, w, h]) - max(l, w, h)) 
    except TypeError:
        return 0

def get_dimensions(s):
    try:
        return map(int, s.split('x'))
    except ValueError:
        return None
    
if __name__ == '__main__':
    area = 0
    length = 0
    for line in fileinput.input():
        area += area_required(line)
        length += length_required(line)
    print 'Wrapping paper required: %i' % area
    print 'Ribbon required: %i' % length
