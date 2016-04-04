#!/usr/bin/env python

import fileinput
import re

class Wire(object):
    def __init(self):
        self._output = None
        self._cmd = None
        self._input1 = None
        self._input2 = None

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
        self._input1 = value

    @input2.setter
    def input2(self, value):
        self._input2 = value

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
    
def evaluate(value):
    if type(value) is int:
        return value
    else:
        if value.cmd == 'NOT':
            return ~evaluate(value.input1) & 0xffff
        if value.cmd == 'AND':
            return value.input1 & value.input2
        if value.cmd == 'OR':
            return value.input1 | value.input2
        if value.cmd == 'LSHIFT':
            return (value.input1 << value.input2) & 0xffff
        if value.cmd == 'RSHIFT':
            return (value.input1 >> value.input2) & 0xffff
        if not value.cmd:
            return evaluate(value.input1)
    return None
    
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

def value(v):
    try:
        return int(v)
    except (ValueError, TypeError):
        return v

def function(s):
    return s

if __name__ == '__main__':
    d = dict()
    for line in fileinput.input():
        id, cmd, in1, in2 = parse_input(line.strip())
        if id:
            w = Wire()
            w.output = id
            w.cmd = cmd
            w.input1 = evaluate(value(in1))
            if in2:
                w.input2 = evaluate(value(in2))
            d[id] = w
    for wire in d.itervalues():
        print wire.output, '=', evaluate(wire)
'''
w = Wire()
w.output = 'a'
w.cmd = 'NOT'
w.input1 = 255
print evaluate(w)
'''
