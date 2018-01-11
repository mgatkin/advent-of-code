#!/usr/bin/env python

import json
import fileinput

def function1(d): 
    j = json.loads(d)
    if type(j) == list:
        return sum(j)
    
def function2(d): 
    return int(d)
    
if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        print 'Executing function1 on line', (n + 1), 'returned ', function1(line)
        print 'Executing function2 on line', (n + 1), 'returned ', function2(line)
