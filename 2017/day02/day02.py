#!/usr/bin/env python

import fileinput

def linediff(d):
    data = map(int, d.strip().split('\t'))
    return max(data) - min(data)

def checksum(d, f):
    total = 0
    for data in d.strip().split('\n'):
        total += f(data)
    return total

def linediv(d): 
    data = map(int, d.strip().split('\t'))
    for n in data:
        subset = list(data)
        subset.remove(n)
        for s in subset:
            if n % s == 0:
                return n / s
    return 0
    
if __name__ == '__main__':
    linediffs = []
    lines = []
    for n, line in enumerate(fileinput.input()):
        lines.append(line)
        linediffs.append(linediff(line))
        print 'linediff of line', n, 'is', linediffs[n]
    print 'checksum is', checksum(''.join(lines), linediff)

    linedivs = []
    for n, line in enumerate(fileinput.input()):
        linedivs.append(linediv(line))
        print 'linediv of line', n, 'is', linedivs[n]
    print 'checksum is', checksum(''.join(lines), linediv)
