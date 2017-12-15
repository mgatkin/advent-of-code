#!/usr/bin/env python

import unittest

from day02 import linediff, linediv, checksum

class TestDay02(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(linediff('5\t1\t9\t5'), 8)
        self.assertEqual(linediff('7\t5\t3'), 4)
        self.assertEqual(linediff('2\t4\t6\t8'), 6)
        self.assertEqual(checksum('5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8', linediff), 18)

    def test_part_two(self):
        self.assertEqual(linediv('5\t9\t2\t8'), 4)
        self.assertEqual(linediv('9\t4\t7\t3'), 3)
        self.assertEqual(linediv('3\t8\t6\t5'), 2)
        self.assertEqual(checksum('5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5', linediv), 9)

if __name__ == '__main__':
    unittest.main()
