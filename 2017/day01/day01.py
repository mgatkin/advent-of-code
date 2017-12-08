#!/usr/bin/env python

import fileinput

def captcha(d): 
    sum = 0
    length = len(d.strip())
    for i, c in enumerate(d.strip()):
        index = (i + 1) % length
        if d[i] == d[index]:
            sum += int(d[i])
    return sum
    
def invcaptcha(d): 
    sum = 0
    length = len(d.strip())
    for i, c in enumerate(d.strip()):
        index = (i + length / 2) % length
        if d[i] == d[index]:
            sum += int(d[i])
    return sum

if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        print 'Captcha for line', n + 1, 'is', captcha(line)
        print 'Inverse captcha for line', n + 1, 'is', invcaptcha(line)
