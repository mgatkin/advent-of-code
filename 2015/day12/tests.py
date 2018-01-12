#!/usr/bin/env python

import unittest

from day12 import traverse

class TestDay12(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(traverse([1,2,3]), 6)
        self.assertEqual(traverse({"a":2,"b":4}), 6)
        self.assertEqual(traverse([[[3]]]), 3)
        self.assertEqual(traverse({"a":{"b":4},"c":-1}), 3)
        self.assertEqual(traverse({"a":[-1,1]}), 0)
        self.assertEqual(traverse([-1,{"a":[1]}]), 0)
        self.assertEqual(traverse([]), 0)
        self.assertEqual(traverse({}), 0)

if __name__ == '__main__':
    unittest.main()
