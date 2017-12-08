#!/bin/bash
if [ ! -d $1 ]; then
    echo Directory $1 does not exist
    exit 1
fi

if [ -d $1/day$2 ]; then
    echo Directory $1/day$2 already exists
    exit 1
fi

mkdir $1/day$2

cat << EOF > $1/day$2/day$2.py
#!/usr/bin/env python

import fileinput

def function1(d): 
    return int(d)
    
def function2(d): 
    return int(d)
    
if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        print 'Executing function1 on line', (n + 1), 'returned ', function1(line)
        print 'Executing function2 on line', (n + 1), 'returned ', function2(line)
EOF

cat << EOF >> $1/day$2/tests.py
#!/usr/bin/env python

import unittest

from day$2 import function1, function2

class TestDay$2(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(function1('0'), 0)

    def test_part_two(self):
        self.assertEqual(function2('0'), 0)

if __name__ == '__main__':
    unittest.main()
EOF

chmod +x $1/day$2/day$2.py
chmod +x $1/day$2/tests.py
