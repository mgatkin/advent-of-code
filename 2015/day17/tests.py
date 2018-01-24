#!/usr/bin/env python

import unittest

from day17 import number_of_combinations, minimum_containers

class TestDay17(unittest.TestCase):
    def test_part_one(self):
        data = [ 20, 15, 10, 5, 5 ]
        (number, combinations) = number_of_combinations(data, 25)
        self.assertEqual(number, 4)
        (size, minimum) = minimum_containers(combinations)
        self.assertEqual(minimum, 3)

if __name__ == '__main__':
    unittest.main()
