#!/usr/bin/env python

import unittest

from day02 import linediff, checksum

class TestDay02(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(linediff('5\t1\t9\t5'), 8)
        self.assertEqual(linediff('7\t5\t3'), 4)
        self.assertEqual(linediff('2\t4\t6\t8'), 6)
        #self.assertEqual(checksum('5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8'), 18)

#    def test_part_two(self):
#        self.assertEqual(function2('0'), 0)

if __name__ == '__main__':
    unittest.main()
