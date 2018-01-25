#!/usr/bin/env python

import unittest

from day18 import build_map, next_state, get_state, count_lights_on

class TestDay18(unittest.TestCase):
    d = [ '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..' ]
    m = [
            [ 0, 1, 0, 1, 0, 1 ],
            [ 0, 0, 0, 1, 1, 0 ],
            [ 1, 0, 0, 0, 0, 1 ],
            [ 0, 0, 1, 0, 0, 0 ],
            [ 1, 0, 1, 0, 0, 1 ],
            [ 1, 1, 1, 1, 0, 0 ]
            ]
    results = [
            [ '..##..', '..##.#', '...##.', '......', '#.....', '#.##..' ],
            [ '..###.', '......', '..###.', '......', '.#....', '.#....' ],
            [ '...#..', '......', '...#..', '..##..', '......', '......' ]
            ]
    def test_build_map(self):
        data = build_map(self.d)
        self.assertEqual(data, self.m)

    def test_get_state(self):
        self.assertEqual(get_state(self.m), self.d)

    def test_next_state(self):
        self.assertEqual(get_state(next_state(build_map(self.d))), self.results[0])
        self.assertEqual(get_state(next_state(build_map(self.results[0]))), self.results[1])
        self.assertEqual(get_state(next_state(build_map(self.results[1]))), self.results[2])
        self.assertEqual(count_lights_on(next_state(build_map(self.results[1]))), 4)

if __name__ == '__main__':
    unittest.main()
