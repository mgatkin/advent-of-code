#!/usr/bin/env python

import unittest

from circuit import parse_input, evaluate, Wire

class TestCircuit(unittest.TestCase):
    def test_parsing(self):
        self.assertEqual(parse_input('1 -> a'), ('a', None, '1', None))
        self.assertEqual(parse_input('b -> a'), ('a', None, 'b', None))
        self.assertEqual(parse_input('NOT 1 -> a'), ('a', 'NOT', '1', None))
        self.assertEqual(parse_input('NOT b -> a'), ('a', 'NOT', 'b', None))
        self.assertEqual(parse_input('b OR c -> a'), ('a', 'OR', 'b', 'c'))
        self.assertEqual(parse_input('b AND c -> a'), ('a', 'AND', 'b', 'c'))
        self.assertEqual(parse_input('b LSHIFT 1 -> a'), ('a', 'LSHIFT', 'b', '1'))
        self.assertEqual(parse_input('b RSHIFT 1 -> a'), ('a', 'RSHIFT', 'b', '1'))

    def test_wire(self):
        w = Wire()
        w.output = 'a'
        w.cmd = None
        w.input1 = 1
        w.input2 = None
        self.assertEqual(evaluate(w), 1)

if __name__ == '__main__':
    unittest.main()

