from copy import deepcopy
from functools import reduce

from res.utils import parse_input


def add_numbers(n1, n2):
    out = ['0']*len(n1)

    if isinstance(n1, str):
        n1 = list(n1)
    if isinstance(n2, str):
        n2 = list(n2)

    for i in range(len(n1)):
        out[i] = (str(int(n1[i])+int(n2[i])))

    return out


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')

    median = len(input_lines)/2
    res = reduce(add_numbers, input_lines)

    gamma = ''
    epsilon = ''

    for i in res:
        if int(i) > median:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    lines_filtered = deepcopy(input_lines)
    lines_next_set = []
    idx = 0

    while len(lines_filtered) != 1:
        median = len(lines_filtered) / 2
        res = reduce(add_numbers, lines_filtered)

        if int(res[idx]) >= median:
            oxygen_gen = '1'
        else:
            oxygen_gen = '0'

        for line in lines_filtered:
            if line[idx] == oxygen_gen:
                lines_next_set.append(line)

        lines_filtered = deepcopy(lines_next_set)
        lines_next_set = []
        idx += 1

    oxygen_gen = lines_filtered.pop()

    lines_filtered = deepcopy(input_lines)
    lines_next_set = []
    idx = 0

    while len(lines_filtered) != 1:
        median = len(lines_filtered) / 2
        res = reduce(add_numbers, lines_filtered)

        if int(res[idx]) >= median:
            scrubber_rat = '0'
        else:
            scrubber_rat = '1'

        for line in lines_filtered:
            if line[idx] == scrubber_rat:
                lines_next_set.append(line)

        lines_filtered = deepcopy(lines_next_set)
        lines_next_set = []
        idx += 1

    scrubber_rat = lines_filtered.pop()

    return int(oxygen_gen, 2) * int(scrubber_rat, 2)


if __name__ == "__main__":
    puzzle_input = parse_input(day=3)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    