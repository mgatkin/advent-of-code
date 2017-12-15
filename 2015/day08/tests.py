#!/usr/bin/env python

import unittest

from day08 import literal_length, in_memory_length

class TestDay08(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(literal_length(""), 0)
        self.assertEqual(literal_length("abc"), 3)
        self.assertEqual(literal_length("aaa\"aaa"), 7)
        self.assertEqual(literal_length("\x27"), 1)

#    def test_part_two(self):
#        self.assertEqual(function2('0'), 0)

if __name__ == '__main__':
    unittest.main()
