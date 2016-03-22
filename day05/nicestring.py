#!/usr/bin/env python

import fileinput
import re
import sys
from os.path import basename

def process_rule(rule, s):
    for exp in rule:
        rexp = re.compile(exp)
        if rexp.match(s) is None:
            return 'naughty'
    return 'nice'

def rule_set_1(s):
    return process_rule([ r'(.*[aeiou]){3}', r'.*([a-z])\1', r'(?!.*((ab)|(cd)|(pq)|(xy)))' ], s)


def rule_set_2(s):
    return process_rule([ r'.*([a-z]{2}).*\1', r'.*([a-z]).\1' ], s)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage:', basename(__file__), '<input file>'
        sys.exit(0)

    nice_lines = [ ]
    rules = [ rule_set_1, rule_set_2 ]
    for index, rule in enumerate(rules):
        nice_lines.append(0)
        for line in fileinput.input():
            if rule(line) == 'nice':
                nice_lines[index] += 1
        print 'Rule set', index + 1, 'found', nice_lines[index], 'nice line(s) in', fileinput.filename()

