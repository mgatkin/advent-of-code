#!/usr/bin/env python

import unittest

from day19 import build_tables, process_substitutions, process_molecules

class TestDay19(unittest.TestCase):
    i = [ 'H => HO\n', 'H => OH\n', 'O => HH\n', '\n', 'HOH\n', 'HOHOHO' ]
    e = [ 'HOH', 'HOHOHO' ]
    s = { 'H':[ 'HO', 'OH' ], 'O':[ 'HH' ] }
    results = [
            [ 'HOOH', 'HOHO', 'OHOH', 'HHHH' ],
            [ 'HOOHOHO', 'HOHOOHO', 'HOHOHOO', 'OHOHOHO', 'HHHHOHO', 'HOHHHHO', 'HOHOHHH' ]
            ]

    def test_build_tables(self):
        self.assertEqual(build_tables(self.i), (self.s, self.e))

    def test_process_substitutions(self):
        self.assertEqual(process_substitutions(self.e[0], self.s), self.results[0])
        self.assertEqual(process_substitutions(self.e[1], self.s), self.results[1])

    def test_process_molecules(self):
        self.assertEqual(process_molecules(self.e, self.s), self.results)

if __name__ == '__main__':
    unittest.main()
