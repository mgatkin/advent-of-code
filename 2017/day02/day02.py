#!/usr/bin/env python

import fileinput

def linediff(d):
    data = map(int, d.strip().split('\t'))
    return max(data) - min(data)

def function2(d): 
    return int(d)
    
if __name__ == '__main__':
    linediffs = []
    for n, line in enumerate(fileinput.input()):
        linediffs.append(linediff(line))
        print 'linediff of line', n, 'is', linediffs[n]
    print 'checksum is', sum(linediffs)
