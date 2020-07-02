#!/usr/bin/env python

import sys


def number_of_parameters_for_opcode(op):
    if op == 1 or op == 2:
        return 3
    elif op == 3 or op == 4:
        return 1
    elif op == 99:
        return 0
    else:
        return None


def parse_command(data):
    opcode = data[0] % 100
    parameters = []
    length = number_of_parameters_for_opcode(opcode) + 1
    if length == 4:
        cmd = '%05d' % data[0]
        parameters.append((cmd[2], data[1]))
        parameters.append((cmd[1], data[2]))
        parameters.append((cmd[0], data[3]))
    elif length == 2:
        cmd = '%03d' % data[0]
        parameters.append((cmd[0], data[1]))
    elif length == 1:
        cmd = '%02d' % data[0]
    else:
        cmd = None
    return opcode, parameters, length


def get_value(mode, value, buffer):
    if mode == '0':
        return buffer[value]
    elif mode == '1':
        return value
    else:
        return None


def execute_command(command, parameters, data_buffer):
    if command == 1:
        value1 = get_value(parameters[0][0], parameters[0][1], data_buffer)
        value2 = get_value(parameters[1][0], parameters[1][1], data_buffer)
        value3 = parameters[2][1]
        data_buffer[value3] = value1 + value2
    elif command == 2:
        value1 = get_value(parameters[0][0], parameters[0][1], data_buffer)
        value2 = get_value(parameters[1][0], parameters[1][1], data_buffer)
        value3 = parameters[2][1]
        data_buffer[value3] = value1 * value2
    else:
        return None


def parse_input(data):
    cmd = None
    index = 0
    buffer = data[:]
    while len(data) and cmd != 99:
        cmd, parms, cmd_length = parse_command(data[:4])
        execute_command(cmd, parms, buffer)
        index = index + cmd_length
        data = buffer[index:]
    return buffer


if __name__ == '__main__':
    try:
        with open(sys.argv[1]) as f:
            raw_data = [int(s) for s in f.readline().split(',')]

            # Part 1
            print(parse_input(raw_data))

            # Part 2
            # Not yet implemented

    except IndexError:
        print('Syntax: ' + sys.argv[0] + ' <input file>')
