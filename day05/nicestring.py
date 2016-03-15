#!/usr/bin/env python

import fileinput
import re
import sys
from os.path import basename

def set_of_rules_1(s):
    re1 = re.compile(r'.*[aeiou].*[aeiou].*[aeiou]')
    re2 = re.compile(r'.*([a-z])\1')
    re3 = re.compile(r'.*((ab)|(cd)|(pq)|(xy))')
    if re1.match(s) is not None and re2.match(s) is not None and re3.match(s) is None:
        return 'nice'
    else:
        return 'naughty'


def set_of_rules_2(s):
    re1 = re.compile(r'.*([a-z][a-z]).*\1')
    re2 = re.compile(r'.*([a-z]).\1')
    if re1.match(s) is not None and re2.match(s) is not None:
        return 'nice'
    else:
        return 'naughty'


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage:', basename(__file__), '<input file>'
        sys.exit(0)

    nice_lines = [ ]
    rules = [ set_of_rules_1, set_of_rules_2 ]
    for index, rule in enumerate(rules):
        nice_lines.append(0)
        for line in fileinput.input():
            if rule(line) == 'nice':
                nice_lines[index] += 1
        print 'Rule set', index + 1, 'found', nice_lines[index], 'nice line(s) in', fileinput.filename()

