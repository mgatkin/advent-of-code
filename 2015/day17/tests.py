#!/usr/bin/env python

import unittest

from day17 import number_of_combinations

class TestDay17(unittest.TestCase):
    def test_part_one(self):
        data = [ 20, 15, 10, 5, 5 ]
        self.assertEqual(number_of_combinations(data, 25), 4)

if __name__ == '__main__':
    unittest.main()
