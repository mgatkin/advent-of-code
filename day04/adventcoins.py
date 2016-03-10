#!/usr/bin/env python

import fileinput
from md5 import md5

def advent_hash(s):
    return md5(s).hexdigest()

def mine_advent_coin(s):
    number = 0
    while advent_hash(s + str(number))[:5] != '00000':
        number += 1
    return number

if __name__ == '__main__':
    for line in fileinput.input():
        number = str(mine_advent_coin(line))
        hash_of_number = advent_hash(line + number)
        print 'MD5 hash of' + line.strip() + number + 'starts with ' + hash_of_number[:11] + '...'

