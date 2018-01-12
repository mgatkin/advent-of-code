#!/usr/bin/env python

import json
import fileinput

def traverse(d):
    total = 0
    if type(d) is dict:
        values = [ v for v in d.values() ]
        if "red" not in values:
            total = total + traverse(values)
    elif type(d) is list:
        for i in d:
            total = total + traverse(i)
    else:
        try:
            total = total + int(d)
        except ValueError:
            pass
    return total

if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        print 'Executing traverse on line', str(n + 1), 'returned', traverse(json.loads(line))
