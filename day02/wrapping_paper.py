#!/usr/bin/env python

import fileinput

def area_required(s):
    try:
        l, w, h = map(int, s.split('x'))
        a = [ l*w, l*h, w*h ]
        return 2*sum(a) + min(a)
    except ValueError:
        return None

if __name__ == '__main__':
    area = 0
    for line in fileinput.input():
        present = area_required(line)
        if present is not None:
            area += present
    print 'Wrapping paper required: %i' % area
