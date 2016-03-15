#!/usr/bin/env python

import fileinput
import re

def set_of_rules_1(s):
    re1 = re.compile(r'.*[aeiou].*[aeiou].*[aeiou]')
    re2 = re.compile(r'.*([a-z])\1')
    re3 = re.compile(r'.*((ab)|(cd)|(pq)|(xy))')
    if re1.match(s) is not None and re2.match(s) is not None and re3.match(s) is None:
        return 'nice'
    else:
        return 'naughty'


if __name__ == '__main__':
    nice_lines = [ 0 ]
    rules = [ set_of_rules_1 ]
    for index, rule in enumerate(rules):
        for line in fileinput.input():
            if rule(line) == 'nice':
                nice_lines[index] += 1
        print 'Rule set', index, 'found', nice_lines[index], 'nice line(s) in', fileinput.filename()

