#!/usr/bin/env python

import fileinput
from md5 import md5

def advent_hash(s):
    return md5(s).hexdigest()

def mine_advent_coin(s, stars):
    number = 0
    while advent_hash(s + str(number))[:stars] != '0' * stars:
        number += 1
    return number

if __name__ == '__main__':
    for line in fileinput.input():
        secret_key = line.strip()
        for number_of_zeroes in 5, 6:
            number = str(mine_advent_coin(secret_key, number_of_zeroes))
            hash_of_number = advent_hash(secret_key + number)
            print 'MD5 hash of ' + secret_key + number + ' starts with ' + \
                hash_of_number[:(number_of_zeroes + 6)] + '...'

