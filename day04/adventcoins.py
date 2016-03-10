#!/usr/bin/env python

import fileinput
from md5 import md5

def advent_hash(s):
    return md5(s).hexdigest()

if __name__ == '__main__':
    for line in fileinput.input():
        print line

