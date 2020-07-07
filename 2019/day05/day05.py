#!/usr/bin/env python

import sys


io_value = None


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
    op_code = data[0] % 100
    parameters = []
    length = number_of_parameters_for_opcode(op_code) + 1
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
    return op_code, parameters, length


def get_value(mode, value, buffer):
    if mode == '0':
        if len(buffer) > value:
            return buffer[value]
        else:
            return None
    elif mode == '1':
        return value
    else:
        return None


def execute_command(command, parameters, data_buffer):
    global io_value
    if command == 1:
        value1 = get_value(parameters[0][0], parameters[0][1], data_buffer)
        value2 = get_value(parameters[1][0], parameters[1][1], data_buffer)
        index = parameters[2][1]
        if index is not None:
            while len(data_buffer) < index:
                data_buffer.append(None)
            data_buffer[index] = value1 + value2
    elif command == 2:
        value1 = get_value(parameters[0][0], parameters[0][1], data_buffer)
        value2 = get_value(parameters[1][0], parameters[1][1], data_buffer)
        index = parameters[2][1]
        if index is not None:
            while len(data_buffer) < index:
                data_buffer.append(None)
            data_buffer[index] = value1 * value2
    elif command == 3:
        index = parameters[0][1]
        if index is not None:
            while len(data_buffer) < index:
                data_buffer.append(None)
            data_buffer[index] = io_value
    elif command == 4:
        index = parameters[0][1]
        if index is not None:
            while len(data_buffer) < index:
                data_buffer.append(None)
            io_value = data_buffer[index]


def parse_input(data):
    cmd = None
    index = 0
    buffer = data[:]
    while len(data) and cmd != 99:
        cmd, parameters, cmd_length = parse_command(data[:4])
        execute_command(cmd, parameters, buffer)
        index = index + cmd_length
        data = buffer[index:]
    return buffer


if __name__ == '__main__':
    try:
        with open(sys.argv[1]) as f:
            raw_data = [int(s) for s in f.readline().split(',')]

            if len(sys.argv) > 2:
                io_value = int(sys.argv[2])

            # Part 1
            parse_input(raw_data)
            print(io_value)

            # Part 2
            # Not yet implemented

    except IndexError:
        print('Syntax: ' + sys.argv[0] + ' <input file>')
