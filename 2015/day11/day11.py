#!/usr/bin/env python

import re
import fileinput

def requirement1(d): 
    try:
        if re.search('[a-z]{8}', d).string:
            return True
    except AttributeError:
        return False

def requirement2(d): 
    for c in xrange(24):
        match = re.search(chr(97 + c) + chr(98 + c) + chr(99 + c), d)
        try:
            if match.string:
                return True
        except:
            continue
    return False

def requirement3(d): 
    try:
        if re.search('[iol]', d).string:
            return False
    except AttributeError:
        return True

def requirement4(d): 
    pairs = 0
    for c in xrange(26):
        match = re.search(chr(97 + c) * 2, d)
        try:
            if match.string:
                pairs = pairs + 1
        except:
            continue
    return pairs >= 2

def is_valid(d): 
    return requirement1(d) and requirement2(d) and requirement3(d) and requirement4(d)

def next_password(d):
    if not requirement1(d):
        return None
    length = len(d)
    carry = 1
    index = 7
    while carry and index >= 0:
        next_char = ord(d[index]) + carry
        if next_char > ord('z'):
            next_char = ord('a')
            carry = 1
        elif next_char == ord('i') or next_char == ord('o') or next_char == ord('l'):
            next_char = next_char + 1
            carry = 0
        else:
            carry = 0
        d = d[0:index] + chr(next_char) + d[index + 1:length]
        index = index - 1
    if carry and index < 0:
        d = ''
    return d

def next_valid_password(d):
    if not requirement1(d):
        return None
    if not is_valid(d):
        for index in xrange(len(d)):
            if not requirement3(d[index]):
                next_char = ord(d[index]) + 1
                d = d[0:index] + chr(next_char) + 'a' * (len(d) - 1 - index)
                break

    password = next_password(d)
    while len(password) and not is_valid(password):
        password = next_password(password)
    return password


if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        print 'Executing validate on line', (n + 1), 'returned', next_valid_password(line.strip())
