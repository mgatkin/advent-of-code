#!/usr/bin/env python

import sys
from os.path import basename
import argparse
import re
from collections import OrderedDict

class Wire:
    def __init__(self, output=None, cmd=None, input1=None, input2=None):
        self._output = output
        self._cmd = cmd
        self._input1 = TryInt(input1)
        self._input2 = TryInt(input2)

    def __str__(self):
        return 'output = %-4s <===> cmd = %-6s <===> input1 = %-4s <===> input2 = %-4s' % \
            (self._output, self._cmd, self._input1, self._input2)

    @property
    def output(self):
        return self._output

    @property
    def cmd(self):
        return self._cmd

    @property
    def input1(self):
        return self._input1

    @property
    def input2(self):
        return self._input2

    @output.setter
    def output(self, value):
        self._output = value

    @cmd.setter
    def cmd(self, value):
        self._cmd = value

    @input1.setter
    def input1(self, value):
        self._input1 = TryInt(value)

    @input2.setter
    def input2(self, value):
        self._input2 = TryInt(value)

    @output.deleter
    def output(self):
        del self._output
    
    @cmd.deleter
    def cmd(self):
        del self._cmd
    
    @input1.deleter
    def input1(self):
        del self._input1
    
    @input2.deleter
    def input2(self):
        del self._input2
    
def evaluate(d=dict(), value=None):
    if type(value) is Wire:
        return evaluate(d, value)
    if type(value) is str:
        return evaluate(d, d[value])
    if type(value) is int:
        return value
    if value.cmd == 'NOT':
        return ~(evaluate(d, value.input1)) & 0xffff
    if value.cmd == 'AND':
        return evaluate(d, value.input1) & evaluate(d, value.input2)
    if value.cmd == 'OR':
        return evaluate(d, value.input1) | evaluate(d, value.input2)
    if value.cmd == 'LSHIFT':
        return (evaluate(d, value.input1) << evaluate(d, value.input2)) & 0xffff
    if value.cmd == 'RSHIFT':
        return (evaluate(d, value.input1) >> evaluate(d, value.input2)) & 0xffff
    if not value.cmd:
        return evaluate(d, value.input1)
    
def parse_input(s):
    count = len(s.split())
    output, cmd, input1, input2 = None, None, None, None
    if count == 5:
        input1, cmd, input2, dummy, output = s.split()
    if count == 4:
        cmd, input1, dummy, output = s.split()
    if count == 3:
        input1, dummy, output = s.split()

    return output, cmd, input1, input2

def TryInt(v):
    try:
        return int(v)
    except (ValueError, TypeError, AttributeError):
        return v

def function(s):
    return s

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decipher logic for Advent-Of-Code:  Day 7')
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('wire', nargs='?')
    p = parser.parse_args()

    data = p.infile.readlines()
    d = dict()#OrderedDict()
    for line in data:
        id, cmd, in1, in2 = parse_input(line.strip())
        if id:
            w = Wire(id, cmd, in1, in2)
            d[id] = w
    if p.wire is None:
        for wire in d.itervalues():
            print wire.output, '=', evaluate(d, wire)
    else:
        print 'wire', p.wire, 'is', evaluate(d, d[p.wire])

