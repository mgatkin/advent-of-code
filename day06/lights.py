#!/usr/bin/env python

import fileinput
import re
import sys
from os.path import basename

def parse_instruction(s):
    r = re.search('(.*) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$', s)
    return (r.group(1), [[int(r.group(2)),int(r.group(3))],[int(r.group(4)),int(r.group(5))]])

def set_light(arr, m, f):
    xorg = m[0][0]
    yorg = m[0][1]
    xend = m[1][0]
    yend = m[1][1]
    deltax = xend - xorg + 1
    deltay = yend - yorg + 1
    for x in xrange(deltax):
        for y in xrange(deltay):
            arr[x + xorg][y + yorg] = f(arr[x + xorg][y + yorg])
    return arr
    
def toggle(arr, m):
    return set_light(arr, m, lambda x: 1 - x)

def turn_on(arr, m):
    return set_light(arr, m, lambda x: 1)

def turn_off(arr, m):
    return set_light(arr, m, lambda x: 0)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage:', basename(__file__), '<input file>'
        sys.exit(0)

    line_no = 0
    lights = [[0 for x in xrange(1000)] for x in xrange(1000)] 
    for line in fileinput.input():
        line_no = line_no + 1
        instruction, m = parse_instruction(line)
        if instruction == 'toggle':
            toggle(lights, m)
        if instruction == 'turn on':
            turn_on(lights, m)
        if instruction == 'turn off':
            turn_off(lights, m)
    count = 0
    for row, data in enumerate(lights):
        count = count + sum(data)
    print count, 'light(s) on'

