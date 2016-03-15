#!/usr/bin/env python

import unittest

from day05 import nicestring

class TestFunction(unittest.TestCase):
    def test_nicestring(self):
        self.assertEqual(nicestring('ugknbfddgicrmopn'), 'nice')
        self.assertEqual(nicestring('aaa'), 'nice')
        self.assertEqual(nicestring('jchzalrnumimnmhp'), 'naughty')
        self.assertEqual(nicestring('haegwjzuvuyypxyu'), 'naughty')
        self.assertEqual(nicestring('dvszwmarrgswjxmb'), 'naughty')


if __name__ == '__main__':
    unittest.main()

