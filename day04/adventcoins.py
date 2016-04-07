#!/usr/bin/env python

import fileinput
from md5 import md5
from time import time

def advent_hash(s):
    return md5(s).hexdigest()

def mine_advent_coin(key, zeroes):
    number = 0
    while advent_hash(key + str(number))[:zeroes] != '0' * zeroes:
        number += 1
    return number

if __name__ == '__main__':
    for line in fileinput.input():
        key = line.strip()
        for zeroes in 5, 6:
            start_time = time()
            number = str(mine_advent_coin(key, zeroes))
            hash_result = advent_hash(key + number)
            print 'MD5 hash of ' + key + number + ' starts with ' + \
                hash_result[:(zeroes + 6)] + \
                '... (Ran in %.3f seconds)' % (time() - start_time)

