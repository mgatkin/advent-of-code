#!/usr/bin/env python

import unittest

from day03 import distance

class TestDay03(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(distance(1), 0)
        self.assertEqual(distance(12), 3)
        self.assertEqual(distance(23), 2)
        self.assertEqual(distance(1024), 31)
        self.assertEqual(distance(1), 0)
        self.assertEqual(distance(2), 1)
        self.assertEqual(distance(3), 2)
        self.assertEqual(distance(4), 1)
        self.assertEqual(distance(5), 2)
        self.assertEqual(distance(6), 1)
        self.assertEqual(distance(7), 2)
        self.assertEqual(distance(8), 1)
        self.assertEqual(distance(9), 2)
        self.assertEqual(distance(10), 3)

if __name__ == '__main__':
    unittest.main()
