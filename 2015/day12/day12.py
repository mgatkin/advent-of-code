#!/usr/bin/env python

import json
import fileinput

def function1(d): 
    print d
    j = json.loads(d)
    return type(j)
#    if type(j) == list:
#        return sum(j)

if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        print 'Executing function1 on line', (n + 1), 'returned', function1(line.strip())
