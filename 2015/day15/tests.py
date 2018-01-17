#!/usr/bin/env python

import unittest

from day15 import add_ingredients, cookie_score

class TestDay15(unittest.TestCase):
    def test_part_one(self):
        data = [
                'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8\n',
                'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3\n'
                ]
        ingredients = add_ingredients(data)
        self.assertEqual(cookie_score((44, 56), ingredients), 62842880)
        self.assertEqual(cookie_score((40, 60), ingredients), 57600000)

if __name__ == '__main__':
    unittest.main()
