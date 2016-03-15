#!/usr/bin/env python

import fileinput
import re

def nicestring(s):
    re1 = re.compile(r'.*[aeiou].*[aeiou].*[aeiou]')
    re2 = re.compile(r'.*([a-z])\1')
    re3 = re.compile(r'.*((ab)|(cd)|(pq)|(xy))')
    if re1.match(s) is not None and re2.match(s) is not None and re3.match(s) is None:
        return 'nice'
    else:
        return 'naughty'


if __name__ == '__main__':
    nice_lines = 0
    for line in fileinput.input():
        if nicestring(line) == 'nice':
            nice_lines += 1
    print fileinput.filename(), 'has', nice_lines, 'nice lines'

