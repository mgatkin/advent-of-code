#!/usr/bin/env python

import unittest

from nicestring import set_of_rules_1

class TestFunction(unittest.TestCase):
    def test_nicestring(self):
        self.assertEqual(set_of_rules_1('ugknbfddgicrmopn'), 'nice')
        self.assertEqual(set_of_rules_1('aaa'), 'nice')
        self.assertEqual(set_of_rules_1('jchzalrnumimnmhp'), 'naughty')
        self.assertEqual(set_of_rules_1('haegwjzuvuyypxyu'), 'naughty')
        self.assertEqual(set_of_rules_1('dvszwmarrgswjxmb'), 'naughty')


if __name__ == '__main__':
    unittest.main()

