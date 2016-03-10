#!/usr/bin/env python

import unittest

from wrapping_paper import area_required, length_required

class TestDay02(unittest.TestCase):
    def test_area_required(self):
        self.assertEqual(area_required('2x3x4'), 58)
        self.assertEqual(area_required('1x1x10'), 43)
        self.assertEqual(area_required('0x0x0'), 0)
        self.assertEqual(area_required('0x20x0'), 0)
        self.assertEqual(area_required('10x20x0'), 400)
        self.assertEqual(area_required('\n'), 0)
        self.assertEqual(area_required(''), 0)

    def test_length_required(self):
        self.assertEqual(length_required('2x3x4'), 34)
        self.assertEqual(length_required('1x1x10'), 14)
        self.assertEqual(length_required('0x0x0'), 0)
        self.assertEqual(length_required('0x20x0'), 0)
        self.assertEqual(length_required('10x20x0'), 20)
        self.assertEqual(length_required('\n'), 0)
        self.assertEqual(length_required(''), 0)

if __name__ == '__main__':
    unittest.main()

