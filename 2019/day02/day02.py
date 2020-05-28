#!/usr/bin/env python

import sys

def intcode(noun, verb, raw_data):
    data = [ int(i) for i in raw_data ]
    data[1] = noun
    data[2] = verb
    for i in range(int(len(data) / 4)):
        opcode = data[i * 4]
        arg1_position = i * 4 + 1
        arg2_position = i * 4 + 2
        result_position = data[i * 4 + 3]
        arg1 = data[arg1_position]
        arg2 = data[arg2_position]
        data1 = data[arg1]
        data2 = data[arg2]
        if opcode == 1:
            data[result_position] = data1 + data2
        elif opcode == 2:
            data[result_position] = data1 * data2
        elif opcode == 99:
            break
        else:
            print('Invalid opcode')
            break

    return data


def solve():
    for noun in range(100):
        for verb in range(100):
            if intcode(noun, verb, raw_data)[0] == 19690720:
                return(noun, verb)


if __name__ == '__main__':
    try:
        with open(sys.argv[1]) as f:
            raw_data = f.readline().split(',')

            # Part 1
            print(intcode(12, 2, raw_data)[0])

            # Part 2
            noun, verb = solve()
            print(noun * 100 + verb)

    except IndexError:
        print('Syntax: ' + sys.argv[0] + ' <input file>')

