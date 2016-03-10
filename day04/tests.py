#!/usr/bin/env python

import unittest

from adventcoins import advent_hash

class TestAdventCoins(unittest.TestCase):
    def test_advent_hash(self):
        self.assertEqual(advent_hash('abcdef609043')[:5], '00000')
        self.assertEqual(advent_hash('pqrstuv1048970')[:5], '00000')

if __name__ == '__main__':
    unittest.main()

