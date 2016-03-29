#!/usr/bin/env python

import fileinput
import numpy as np

def parse_instruction(s):
    return s

def toggle(arr, m):
    arr[m[0][0]:(m[1][0]+1),m[0][1]:(m[1][1]+1)] ^= np.ones((m[1][0]-m[0][0]+1,m[1][1]-m[0][1]+1),np.bool_)
    return arr

def turn_on(arr, m):
    print arr, m
    print m[0][0], m[1][0], m[0][1], m[1][1]
    arr[m[0][0]:(m[1][0]+1),m[0][1]:(m[1][1]+1)] = np.ones((m[1][0]-m[0][0]+1,m[1][1]-m[0][1]+1),np.bool_)
    return arr

def turn_off(arr, m):
    arr[m[0][0]:(m[1][0]+1),m[0][1]:(m[1][1]+1)] = np.zeros((m[1][0]-m[0][0]+1,m[1][1]-m[0][1]+1),np.bool_)
    return arr

if __name__ == '__main__':
    for line in fileinput.input():
        print line

