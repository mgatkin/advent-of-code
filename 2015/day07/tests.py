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

    def test_int(self):
        self.assertEqual(evaluate(value=Wire(input1=1)), 1)
        self.assertEqual(evaluate(value=Wire(cmd='NOT', input1=1)), 65534)
        self.assertEqual(evaluate(value=Wire(cmd='OR', input1=1, input2=2)), 3)
        self.assertEqual(evaluate(value=Wire(cmd='OR', input1=1, input2=3)), 3)
        self.assertEqual(evaluate(value=Wire(cmd='OR', input1=3, input2=12)), 15)
        self.assertEqual(evaluate(value=Wire(cmd='AND', input1=1, input2=2)), 0)
        self.assertEqual(evaluate(value=Wire(cmd='AND', input1=3, input2=6)), 2)
        self.assertEqual(evaluate(value=Wire(cmd='AND', input1=15, input2=6)), 6)
        self.assertEqual(evaluate(value=Wire(cmd='LSHIFT', input1=1, input2=3)), 8)
        self.assertEqual(evaluate(value=Wire(cmd='LSHIFT', input1=2, input2=4)), 32)
        self.assertEqual(evaluate(value=Wire(cmd='LSHIFT', input1=512, input2=8)), 0)
        self.assertEqual(evaluate(value=Wire(cmd='RSHIFT', input1=256, input2=4)), 16)
        self.assertEqual(evaluate(value=Wire(cmd='RSHIFT', input1=63, input2=4)), 3)
        self.assertEqual(evaluate(value=Wire(cmd='RSHIFT', input1=31, input2=5)), 0)

    def test_int(self):
        d = { 'a': Wire('a', input1=1), 'b': Wire('b', input1=2), 'c': Wire('c', 'OR', 'a', 'b') }
        self.assertEqual(evaluate(d, d['a']), 1)
        self.assertEqual(evaluate(d, d['b']), 2)
        self.assertEqual(evaluate(d, d['c']), 3)

if __name__ == '__main__':
    unittest.main()

