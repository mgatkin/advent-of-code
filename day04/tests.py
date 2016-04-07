#!/usr/bin/env python

import unittest

from adventcoins import advent_hash, mine_advent_coin

class TestAdventCoins(unittest.TestCase):
    def test_advent_hash(self):
        self.assertEqual(advent_hash('abcdef609043')[:5], '00000')
        self.assertEqual(advent_hash('pqrstuv1048970')[:5], '00000')

    def test_mine_advent_coin(self):
        self.assertEqual(mine_advent_coin('abcdef', 5), 609043)
        self.assertEqual(mine_advent_coin('pqrstuv', 5), 1048970)

if __name__ == '__main__':
    unittest.main()

