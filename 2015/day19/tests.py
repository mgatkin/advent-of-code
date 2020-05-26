#!/usr/bin/env python

import unittest

from day19 import flatten, build_tables, process_substitutions, process_molecules

class TestDay19(unittest.TestCase):
    i = [ 'e => H\n', 'e => O\n', 'H => HO\n', 'H => OH\n', 'O => HH\n', '\n', 'e\n', 'HOH\n', 'HOHOHO' ]
    e = [ 'e', 'HOH', 'HOHOHO' ]
    s = { 'e':[ 'H', 'O' ], 'H':[ 'HO', 'OH' ], 'O':[ 'HH' ] }
    results = [
            [ 'H', 'O' ],
            [ 'HOOH', 'HOHO', 'OHOH', 'HHHH' ],
            [ 'HOOHOHO', 'HOHOOHO', 'HOHOHOO', 'OHOHOHO', 'HHHHOHO', 'HOHHHHO', 'HOHOHHH' ]
            ]
    steps = [
            [ 'e' ],
            [ 'H', 'O'],
            [ 'HO', 'OH', 'HH' ],
            [ 'HOO', 'OHO', 'HHH', 'OOH', 'HOH', 'HHO', 'OHH' ],
            ]

    def test_build_tables(self):
        self.assertEqual(build_tables(self.i), (self.s, self.e))

    def test_process_substitutions(self):
        self.assertEqual(process_substitutions(self.e[0], self.s), self.results[0])
        self.assertEqual(process_substitutions(self.e[1], self.s), self.results[1])
        self.assertEqual(process_substitutions(self.e[2], self.s), self.results[2])

    def test_process_molecules(self):
        self.assertEqual(process_molecules(self.e, self.s), self.results)

    def test_fabricate_molecule(self):
        self.assertEqual(flatten(process_molecules(self.steps[0], self.s)), self.steps[1])
        self.assertEqual(flatten(process_molecules(self.steps[1], self.s)), self.steps[2])
        self.assertEqual(flatten(process_molecules(self.steps[2], self.s)), self.steps[3])

if __name__ == '__main__':
    unittest.main()
