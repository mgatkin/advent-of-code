#!/usr/bin/env python

import unittest

from day02 import wrapping_paper

class TestDay02(unittest.TestCase):
    def test_wrapping_paper(self):
        self.assertEqual(wrapping_paper('2x3x4'), 58)
        self.assertEqual(wrapping_paper('1x1x10'), 43)
        self.assertEqual(wrapping_paper(''), None)
        self.assertEqual(wrapping_paper('\n'), None)

if __name__ == '__main__':
    unittest.main()

