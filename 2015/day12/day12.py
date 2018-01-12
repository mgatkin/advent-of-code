#!/usr/bin/env python

import json
import fileinput

def traverse(d, exclude = None):
    total = 0
    if type(d) is dict:
        values = [ v for v in d.values() ]
        if exclude not in values:
            total = total + traverse(values, exclude)
    elif type(d) is list:
        for i in d:
            total = total + traverse(i, exclude)
    else:
        try:
            total = total + int(d)
        except ValueError:
            pass
    return total

if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        print 'Executing traverse on line', str(n + 1), 'returned', traverse(json.loads(line))
        print 'Executing traverse on line', str(n + 1), '(excluding "red") returned', traverse(json.loads(line), "red")
