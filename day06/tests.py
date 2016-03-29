#!/usr/bin/env python

import unittest

from lights import parse_instruction, turn_on, turn_off, toggle

class TestFunction(unittest.TestCase):
    def test_set_lights(self):
        self.assertEqual(turn_on(
            [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ],
            [ [ 1, 1 ], [ 1, 1 ] ]),
            [ [ 0, 0, 0 ], [ 0, 1, 1 ], [ 0, 1, 1 ] ])

        self.assertEqual(turn_on(
            [ [ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ] ],
            [ [ 1, 1 ], [ 1, 1 ] ]),
            [ [ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ] ])

        self.assertEqual(turn_off(
            [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ],
            [ [ 1, 1 ], [ 1, 1 ] ]),
            [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ])

        self.assertEqual(turn_off(
            [ [ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ] ],
            [ [ 1, 1 ], [ 1, 1 ] ]),
            [ [ 1, 1, 1 ], [ 1, 0, 0 ], [ 1, 0, 0 ] ])

        self.assertEqual(toggle(
            [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ],
            [ [ 1, 1 ], [ 1, 1 ] ]),
            [ [ 0, 0, 0 ], [ 0, 1, 1 ], [ 0, 1, 1 ] ])

        self.assertEqual(toggle(
            [ [ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ] ],
            [ [ 1, 1 ], [ 1, 1 ] ]),
            [ [ 1, 1, 1 ], [ 1, 0, 0 ], [ 1, 0, 0 ] ])

    def test_parsing(self):
        self.assertEqual(parse_instruction('turn on 1,1 through 2,2'), 'turn on 1,1 through 2,2'),
#        self.assertEqual(parse_instruction('turn on 1,1 through 2,2'),
#            [ [ 0, 0, 0 ], [ 0, 1, 1 ], [ 0, 1, 1 ] ])

if __name__ == '__main__':
    unittest.main()

