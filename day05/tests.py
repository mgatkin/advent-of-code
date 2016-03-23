#!/usr/bin/env python

import unittest

from nicestring import rule_set_1, rule_set_2

class TestFunction(unittest.TestCase):
    def test_rule_set_1(self):
        self.assertEqual(rule_set_1('ugknbfddgicrmopn'), True)
        self.assertEqual(rule_set_1('aaa'), True)
        self.assertEqual(rule_set_1('jchzalrnumimnmhp'), False)
        self.assertEqual(rule_set_1('haegwjzuvuyypxyu'), False)
        self.assertEqual(rule_set_1('dvszwmarrgswjxmb'), False)

    def test_rule_set_2(self):
        self.assertEqual(rule_set_2('qjhvhtzxzqqjkmpb'), True)
        self.assertEqual(rule_set_2('xxyxx'), True)
        self.assertEqual(rule_set_2('uurcxstgmygtbstg'), False)
        self.assertEqual(rule_set_2('ieodomkazucvgmuy'), False)


if __name__ == '__main__':
    unittest.main()

