#!/usr/bin/env python

import unittest

from nicestring import set_of_rules_1, set_of_rules_2

class TestFunction(unittest.TestCase):
    def test_rule_set_1(self):
        self.assertEqual(set_of_rules_1('ugknbfddgicrmopn'), 'nice')
        self.assertEqual(set_of_rules_1('aaa'), 'nice')
        self.assertEqual(set_of_rules_1('jchzalrnumimnmhp'), 'naughty')
        self.assertEqual(set_of_rules_1('haegwjzuvuyypxyu'), 'naughty')
        self.assertEqual(set_of_rules_1('dvszwmarrgswjxmb'), 'naughty')

    def test_rule_set_2(self):
        self.assertEqual(set_of_rules_2('qjhvhtzxzqqjkmpb'), 'nice')
        self.assertEqual(set_of_rules_2('xxyxx'), 'nice')
        self.assertEqual(set_of_rules_2('uurcxstgmygtbstg'), 'naughty')
        self.assertEqual(set_of_rules_2('ieodomkazucvgmuy'), 'naughty')


if __name__ == '__main__':
    unittest.main()

