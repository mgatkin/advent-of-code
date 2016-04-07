#!/usr/bin/env python

import fileinput
from enum import Enum

class Move(Enum):
    SANTA = 0
    ROBOT = 1

def count_presents(directions):
    x = 0
    y = 0
    houses_delivered = 1
    grid = { (0, 0) }
    for move in directions:
        x, y = next_house([x, y], move)
        grid.add((x, y))
    return len(grid)

def count_presents_with_robot(directions):
    santa_x = 0
    santa_y = 0
    robot_x = 0
    robot_y = 0
    houses_delivered = 1
    grid = { (0, 0) }
    turn = Move.SANTA
    for move in directions:
        if turn == Move.SANTA:
            santa_x, santa_y = next_house([santa_x, santa_y], move)
            grid.add((santa_x, santa_y))
        else:
            robot_x, robot_y = next_house([robot_x, robot_y], move)
            grid.add((robot_x, robot_y))
        turn = Move(1 - turn.value)
    return len(grid)

def next_house(coords, direction):
    x, y = coords
    if direction == '<':
        x = x - 1
    if direction == '^':
        y = y - 1
    if direction == '>':
        x = x + 1
    if direction == 'v':
        y = y + 1
    return x, y

if __name__ == '__main__':
    for line in fileinput.input():
        print 'Delivered to %i houses' % count_presents(line)
        print 'Delivered to %i houses using Robo-Santa' % count_presents_with_robot(line)

