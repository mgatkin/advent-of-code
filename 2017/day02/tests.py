#!/usr/bin/env python

import unittest

from day02 import function1, function2

class TestDay02(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(function1('0'), 0)

    def test_part_two(self):
        self.assertEqual(function2('0'), 0)

if __name__ == '__main__':
    unittest.main()
