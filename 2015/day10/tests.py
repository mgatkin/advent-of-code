#!/usr/bin/env python

import unittest

from day10 import count_digits

class TestDay10(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(count_digits('1'), '11')
        self.assertEqual(count_digits('11'), '21')
        self.assertEqual(count_digits('21'), '1211')
        self.assertEqual(count_digits('1211'), '111221')
        self.assertEqual(count_digits('111221'), '312211')

if __name__ == '__main__':
    unittest.main()
