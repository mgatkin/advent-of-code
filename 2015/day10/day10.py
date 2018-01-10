#!/usr/bin/env python

import fileinput

def count_digits(d): 
    s = d
    result = ''
    while len(s):
        next_digit = s[0]
        if len(s) > 1:
            pos = 1
            while s[pos] == next_digit:
                pos = pos + 1
            result = result + chr(48 + pos)
            s = s[pos:]
        else:
            result = result + '1'
            break
        result = result + next_digit
    return result
    
if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        print 'Executing count_digits on line', (n + 1), 'returned', count_digits(line)
