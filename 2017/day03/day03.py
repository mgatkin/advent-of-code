#!/usr/bin/env python

from math import ceil, sqrt
import fileinput

def coords(n):
    k = int(ceil((sqrt(n) - 1) / 2))
    t = 2 * k + 1
    m = t**2
    t = t - 1
    if n >= m - t:
        return k - (m - n), -k
    else:
        m = m - t
    if n >= m - t:
        return -k, -k + (m - n)
    else:
        m = m - t
    if n >= m - t:
        return -k + (m - n), k
    else:
        return k, k - (m - n - t)

def distance(n):
    return abs(n[0]) + abs(n[1])

if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        l = int(line.strip())
        print 'Executing spiral on line', (n + 1), 'returned', coords(l), 'and', distance(coords(l))
