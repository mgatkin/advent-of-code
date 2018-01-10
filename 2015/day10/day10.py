#!/usr/bin/env python

import fileinput

def count_digits(d): 
    s = d
    result = ''
    while len(s):
        next_digit = s[0]
        if len(s) > 1:
            pos = 1
            while pos < len(s) and s[pos] == next_digit:
                pos = pos + 1
            result = result + chr(48 + pos)
            s = s[pos:]
        else:
            result = result + '1'
            s = ''
        result = result + next_digit
    return result
    
def process(n, d):
    for i in xrange(n):
        print 'Pass', (i + 1), '...'
        d = count_digits(d)
    return d

if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        try:
            digits, count = line.strip().split()
        except ValueError:
            digits, count = line.strip(), 1
        digits = process(int(count), digits)
        print 'Processing line', (n + 1), 'returned', digits, '( length =', len(digits), ')'
