#!/usr/bin/env python

import fileinput
import re

class Wire:
    def __init__(self, output=None, cmd=None, input1=None, input2=None):
        self._output = output
        self._cmd = cmd
        self._input1 = TryInt(input1)
        self._input2 = TryInt(input2)

    def __str__(self):
        return 'output = %s\ncmd = %s\ninput1 = %s\ninput2 = %s' % \
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
    
    def evaluate(self, value):
        if type(value) is wire:
            return evaluate(value)
        if self._cmd == 'NOT':
            return ~(self._input1) & 0xffff
        if self._cmd == 'AND':
            return self._input1 & self._input2
        if self._cmd == 'OR':
            return self._input1 | self._input2
        if self._cmd == 'LSHIFT':
            return (self._input1 << self._input2) & 0xffff
        if self._cmd == 'RSHIFT':
            return (self._input1 >> self._input2) & 0xffff
        if not self._cmd:
            return self._input1
    
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
    d = dict()
    for line in fileinput.input():
        id, cmd, in1, in2 = parse_input(line.strip())
        if id:
            w = Wire(id, cmd, in1, in2)
            d[id] = w
    print d
    for wire in d.itervalues():
        print wire.output, '=', wire.evaluate()
'''
w = Wire()
w.output = 'a'
w.cmd = 'NOT'
w.input1 = 255
print evaluate(w)
'''