#!/usr/bin/env python

import sys


def fuel(mass):
    return int(mass / 3) - 2


def total_fuel(mass):
    total_fuel = 0
    remaining_mass = mass
    while fuel(remaining_mass) > 0:
        this_fuel = fuel(remaining_mass)
        remaining_mass = this_fuel
        total_fuel += this_fuel
    return total_fuel


if __name__ == '__main__':
    try:
        with open(sys.argv[1]) as f:
            data = f.readlines()

            # Part 1
            print(sum([fuel(int(i)) for i in data]))

            # Part 2
            print(sum([total_fuel(int(i)) for i in data]))

    except IndexError:
        print('Syntax: ' + sys.argv[0] + ' <input file>')

