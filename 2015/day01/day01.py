#!/usr/bin/env python
from __future__ import with_statement

with open('input.txt') as f:
    data = f.readlines()

for puzzle_number, line in enumerate(data):
    ending_floor = line.count('(') - line.count(')')
    pos = 0
    character_number_entering_basement = None
    for index, c in enumerate(line):
        pos = pos + 1 if c is '(' else pos
        pos = pos - 1 if c is ')' else pos
        if pos < 0:
            character_number_entering_basement = index + 1
            break
    
    print '#%d: Ending Floor = %d,' % (puzzle_number + 1, ending_floor),
    if character_number_entering_basement is None:
        print 'Never entered the basement'
    else:
        print 'Entered basement on character %d' % (character_number_entering_basement)

