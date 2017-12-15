#!/usr/bin/env python

import fileinput

def literal_length(d): 
    return len(d)
    
def in_memory_length(d): 
    length = 0
    backslash = False
    skip = 0
    for c in d[1:len(d)-1]:
        if skip:
            skip -= 1
            continue
        if backslash:
            backslash = False
            if c == 'x':
                skip = 2
            else:
                if c == '"':
                    continue
            continue
        elif c == '\\':
            backslash = True
        length += 1
    return length

def encoded_length(d):
    length = 0
    for c in d:
        if c == '"' or c == '\\':
            length += 1
        length += 1
    return length + 2

if __name__ == '__main__':
    s = []
    all_literal_lengths = 0
    all_in_memory_lengths = 0
    all_encoded_lengths = 0
    for n, line in enumerate(fileinput.input()):
        d = line.strip()
        s.append(d)
        all_literal_lengths += literal_length(d)
        all_in_memory_lengths += in_memory_length(d)
        all_encoded_lengths += encoded_length(d)
        print 'literal length of', d, 'is', literal_length(d)
        print 'in-memory length of', d, 'is', in_memory_length(d)
        print 'encoded length of', d, 'is', encoded_length(d)
    print 'sum of literal string lengths is', all_literal_lengths
    print 'sum of in-memory string lengths is', all_in_memory_lengths
    print 'sum of encoded string lengths is', all_encoded_lengths
    print 'Part 1 result is', all_literal_lengths - all_in_memory_lengths
    print 'Part 2 result is', all_encoded_lengths - all_literal_lengths
