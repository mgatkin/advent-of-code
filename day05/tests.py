#!/usr/bin/env python

import unittest

from nicestring import rule_set_1, rule_set_2

class TestFunction(unittest.TestCase):
    def test_rule_set_1(self):
        self.assertEqual(rule_set_1('ugknbfddgicrmopn'), 'nice')
        self.assertEqual(rule_set_1('aaa'), 'nice')
        self.assertEqual(rule_set_1('jchzalrnumimnmhp'), 'naughty')
        self.assertEqual(rule_set_1('haegwjzuvuyypxyu'), 'naughty')
        self.assertEqual(rule_set_1('dvszwmarrgswjxmb'), 'naughty')

    def test_rule_set_2(self):
        self.assertEqual(rule_set_2('qjhvhtzxzqqjkmpb'), 'nice')
        self.assertEqual(rule_set_2('xxyxx'), 'nice')
        self.assertEqual(rule_set_2('uurcxstgmygtbstg'), 'naughty')
        self.assertEqual(rule_set_2('ieodomkazucvgmuy'), 'naughty')


if __name__ == '__main__':
    unittest.main()

