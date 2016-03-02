#!/usr/bin/env python

import unittest

from house_grid import count_presents

class TestDay03(unittest.TestCase):
    def test_count_presents(self):
        self.assertEqual(count_presents('>'), 2)
        self.assertEqual(count_presents('^>v<'), 4)
        self.assertEqual(count_presents('^v^v^v^v^v'), 2)
        self.assertEqual(count_presents(''), 1)

if __name__ == '__main__':
    unittest.main()

