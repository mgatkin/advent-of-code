#!"C:\Program Files\Python38\python.exe"

import fileinput


def has_a_pair_of_matching_adjacent_digits(data, exclude_larger_groups=False):
    for index in range(len(data) - 1):
        if data[index] == data[index + 1]:
            if not exclude_larger_groups:
                return True
            else:
                if index < len(data) - 2:
                    if data[index] != data[index + 2]:
                        if index == 0:
                            return True
                        else:
                            if data[index - 1] != data[index]:
                                return True
                else:
                    if data[index - 1] != data[index]:
                        return True

    return False


def has_decreasing_digits(data):
    for index in range(len(data) - 1):
        if data[index] > data[index + 1]:
            return True


def is_valid_password(password, exclude_larger_groups=False):
    if len(password) != 6:
        return 0

    if not has_a_pair_of_matching_adjacent_digits(password, exclude_larger_groups):
        return 0

    if has_decreasing_digits(password):
        return 0

    # print(password)
    return 1


def process_input_range(valid_range, exclude_larger_groups=False):
    count = 0

    for value in range(valid_range[0], valid_range[1]):
        count = count + is_valid_password(str(value), exclude_larger_groups)

    return count


if __name__ == '__main__':
    file_input = fileinput.input()
    input_range = [int(i) for i in file_input.readline().strip().split('-')]
    print("Part 1: %d" % process_input_range(input_range))
    print("Part 2: %d" % process_input_range(input_range, exclude_larger_groups=True))
