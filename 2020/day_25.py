import re
from collections import Counter, OrderedDict
import itertools
from copy import deepcopy


def part_1(data):
    i = 1
    loop_size = 0
    while i != data[0]:
        loop_size += 1
        i *= 7
        i %= 20201227

    pub_key = data[1]
    i = 1
    for _ in range(loop_size):
        i *= pub_key
        i %= 20201227

    return i


if __name__ == '__main__':
    with open('input/25.txt') as f:
        _lines = [int(_) for _ in f.read().splitlines()]

    print(part_1(_lines))
