#!/usr/bin/env python

import unittest

from day01 import captcha, invcaptcha

class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(captcha('1122'), 3)
        self.assertEqual(captcha('1111'), 4)
        self.assertEqual(captcha('1234'), 0)
        self.assertEqual(captcha('91212129'), 9)

    def test_part_two(self):
        self.assertEqual(invcaptcha('1212'), 6)
        self.assertEqual(invcaptcha('1221'), 0)
        self.assertEqual(invcaptcha('123425'), 4)
        self.assertEqual(invcaptcha('123123'), 12)
        self.assertEqual(invcaptcha('12131415'), 4)

if __name__ == '__main__':
    unittest.main()

