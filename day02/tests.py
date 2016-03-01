#!/usr/bin/env python

import unittest

from day02 import part1

class TestDay02(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1('0'), 0)

if __name__ == '__main__':
    unittest.main()

