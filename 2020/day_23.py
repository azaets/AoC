import re
from collections import Counter, OrderedDict
import itertools
from copy import deepcopy


def circle_idx(idx):
    # data[9 % circle_len]
    return idx % 9


def part_2(data):

    for i in range(max(data), 10**6):
        data.append(i+1)

    # Select current cup (value, idx)
    current_cup = data[0]

    for _ in range(10**7):
        print(_)

        buffer = []

        # Init destination cup
        destination_cup = current_cup - 1

        # Pick up 3 cups clockwise of the current cup
        for i in range(3):
            buffer.append(data[circle_idx(data.index(current_cup) + 1 + i)])

        # Remove picked cups from original circle
        for i in buffer:
            data.pop(data.index(i))

        while True:
            if destination_cup in buffer:
                destination_cup -= 1
            else:
                if destination_cup >= min(data):
                    destination_cup = (destination_cup, data.index(destination_cup))
                else:
                    destination_cup = (max(data), data.index(max(data)))
                break

        for idx, c in enumerate(buffer):
            data.insert(destination_cup[1] + 1 + idx, c)

        current_cup = data[circle_idx(data.index(current_cup) + 1)]

    return data[data.index(1)+1]


def part_1(data):
    # Select current cup (value, idx)
    current_cup = data[0]

    for _ in range(100):
        buffer = []

        # Init destination cup
        destination_cup = current_cup - 1

        # Pick up 3 cups clockwise of the current cup
        for i in range(3):
            buffer.append(data[circle_idx(data.index(current_cup) + 1 + i)])

        # Remove picked cups from original circle
        for i in buffer:
            data.pop(data.index(i))

        while True:
            if destination_cup in buffer:
                destination_cup -= 1
            else:
                if destination_cup >= min(data):
                    destination_cup = (destination_cup, data.index(destination_cup))
                else:
                    destination_cup = (max(data), data.index(max(data)))
                break

        for idx, c in enumerate(buffer):
            data.insert(destination_cup[1] + 1 + idx, c)

        current_cup = data[circle_idx(data.index(current_cup) + 1)]

    out = ''

    for i in range(len(data)-1):
        out += str(data[circle_idx(data.index(1)+1+i)])

    return out


if __name__ == '__main__':
    with open('input/23.txt') as f:
        _lines = [int(i) for i in [_ for _ in f.read().splitlines()][0]]

    # print(part_1(_lines))
    print(part_2(_lines))
