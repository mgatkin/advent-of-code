#!/usr/bin/env python

import unittest

from day03 import coords, distance

class TestDay03(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(coords(1), (0, 0))
        self.assertEqual(coords(12), (2, 1))
        self.assertEqual(coords(23), (0, -2))
        self.assertEqual(coords(1024), (-15, 16))
        self.assertEqual(distance(coords(1)), 0)
        self.assertEqual(distance(coords(12)), 3)
        self.assertEqual(distance(coords(23)), 2)
        self.assertEqual(distance(coords(1024)), 31)
        self.assertEqual(coords(1), (0, 0))
        self.assertEqual(coords(2), (1, 0))
        self.assertEqual(coords(3), (1, 1))
        self.assertEqual(coords(4), (0, 1))
        self.assertEqual(coords(5), (-1, 1))
        self.assertEqual(coords(6), (-1, 0))
        self.assertEqual(coords(7), (-1, -1))
        self.assertEqual(coords(8), (0, -1))
        self.assertEqual(coords(9), (1, -1))
        self.assertEqual(coords(10), (2, -1))
        self.assertEqual(distance(coords(1)), 0)
        self.assertEqual(distance(coords(2)), 1)
        self.assertEqual(distance(coords(3)), 2)
        self.assertEqual(distance(coords(4)), 1)
        self.assertEqual(distance(coords(5)), 2)
        self.assertEqual(distance(coords(6)), 1)
        self.assertEqual(distance(coords(7)), 2)
        self.assertEqual(distance(coords(8)), 1)
        self.assertEqual(distance(coords(9)), 2)
        self.assertEqual(distance(coords(10)), 3)

#    def test_part_two(self):
#        self.assertEqual(function2('0'), 0)

if __name__ == '__main__':
    unittest.main()
