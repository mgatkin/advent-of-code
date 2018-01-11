#!/usr/bin/env python

import unittest

from day12 import function1, function2

class TestDay12(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(function1('[1,2,3]'), 6)
        self.assertEqual(function1('{"a":,2,"b":4}'), 6)
        self.assertEqual(function1('[[[3]]]'), 3)
        self.assertEqual(function1('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(function1('{"a":[-1,1]}'), 0)
        self.assertEqual(function1('[-1,{"a":[1]}]'), 0)
        self.assertEqual(function1('[]'), 0)
        self.assertEqual(function1('{}'), 0)

    def test_part_two(self):
        self.assertEqual(function2('0'), 0)

if __name__ == '__main__':
    unittest.main()
