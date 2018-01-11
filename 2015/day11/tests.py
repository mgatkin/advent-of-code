#!/usr/bin/env python

import unittest

from day11 import is_valid, next_valid_password

class TestDay11(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(is_valid('hijklmmn'), False)
        self.assertEqual(is_valid('abbceffg'), False)
        self.assertEqual(is_valid('abbcegjk'), False)
        self.assertEqual(is_valid('abcdffaa'), True)
        self.assertEqual(is_valid('ghjaabcc'), True)
        self.assertEqual(next_valid_password('abcdefgh'), 'abcdffaa')
        self.assertEqual(next_valid_password('ghijklmn'), 'ghjaabcc')

if __name__ == '__main__':
    unittest.main()


