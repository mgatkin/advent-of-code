#!/usr/bin/env python

import unittest

from wrapping_paper import area_required

class TestDay02(unittest.TestCase):
    def test_wrapping_paper(self):
        self.assertEqual(area_required('2x3x4'), 58)
        self.assertEqual(area_required('1x1x10'), 43)
        self.assertEqual(area_required(''), None)
        self.assertEqual(area_required('\n'), None)

if __name__ == '__main__':
    unittest.main()

