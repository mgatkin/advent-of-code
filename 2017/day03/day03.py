#!/usr/bin/env python

from math import ceil, sqrt
import fileinput

def create_matrix(n):
    if n <= 1:
        return [[ 0 ]]
    size = int(ceil((sqrt(n) - 1) / 2))
    matrix = [[0 for x in range(2 * size + 1)] for y in range(2 * size + 1)]
    x = size
    y = size
    direction = 4
    for i in xrange(n):
        matrix[y][x] = i + 1
        if direction == 1:      # Right
            if matrix[y - 1][x] == 0:
                direction = 2
                y = y - 1
            else:
                x = x + 1
        elif direction == 2:    # Up
            if matrix[y][x - 1] == 0:
                direction = 3
                x = x - 1
            else:
                y = y - 1
        elif direction == 3:    # Left
            if matrix[y + 1][x] == 0:
                direction = 4
                y = y + 1
            else:
                x = x - 1
        else:                   # Down
            if matrix[y][x + 1] == 0:
                direction = 1
                x = x + 1
            else:
                y = y + 1
    return matrix

def distance(n):
    size = int(ceil((sqrt(n) - 1) / 2))
    matrix = create_matrix(n)
    for i in xrange(len(matrix)):
        try:
            return abs(i - size) + abs(matrix[i].index(n) - size)
        except ValueError:
            continue
    return 0

def stress_test(n):
    if n <= 1:
        return 0
    size = int(ceil((sqrt(n) - 1) / 2))
    matrix = [[0 for x in range(2 * size + 3)] for y in range(2 * size + 3)]
    matrix[size][size] = 1
    x = size
    y = size
    direction = 4
    for i in xrange(n):
        if i == 0:
            matrix[y][x] = 1
        else:
            total = sum(matrix[y-1][x-1:x+2]) + sum(matrix[y][x-1:x+2]) + sum(matrix[y+1][x-1:x+2])
            if total >= n:
                return total
            matrix[y][x] = total
        if direction == 1:      # Right
            if matrix[y - 1][x] == 0:
                direction = 2
                y = y - 1
            else:
                x = x + 1
        elif direction == 2:    # Up
            if matrix[y][x - 1] == 0:
                direction = 3
                x = x - 1
            else:
                y = y - 1
        elif direction == 3:    # Left
            if matrix[y + 1][x] == 0:
                direction = 4
                y = y + 1
            else:
                x = x - 1
        else:                   # Down
            if matrix[y][x + 1] == 0:
                direction = 1
                x = x + 1
            else:
                y = y + 1

if __name__ == '__main__':
    for n, line in enumerate(fileinput.input()):
        l = int(line.strip())
        print 'Executing distance on line', (n + 1), 'returned', distance(l)
        print 'Executing stress_test on line', (n + 1), 'returned', stress_test(l)
