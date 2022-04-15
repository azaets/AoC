from res.utils import parse_input
from copy import deepcopy
import numpy as np


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)
    
    count = 0
    hor_lines = []
    ver_lines = []

    for line in input_lines_p1:
        p1, p2 = line.split(' -> ')
        x1, y1 = list(map(int, p1.split(',')))
        x2, y2 = list(map(int, p2.split(',')))

        if x1 == x2:
            ver_lines.append((x1, y1, x2, y2))
        elif y1 == y2:
            hor_lines.append((x1, y1, x2, y2))

    points = set()
    counted_points = set()

    for ll in hor_lines:
        x1, y1, x2, y2 = ll

        const_coord = y1
        for x in range(min(x1, x2), max(x1, x2) + 1):
            p = (x, const_coord)
            if p in points and p not in counted_points:
                count += 1
                counted_points.add(p)
            else:
                points.add(p)

    for ll in ver_lines:
        x1, y1, x2, y2 = ll

        const_coord = x1
        for y in range(min(y1, y2), max(y1, y2) + 1):
            p = (const_coord, y)
            if p in points and p not in counted_points:
                count += 1
                counted_points.add(p)
            else:
                points.add(p)

    return count


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)
    
    count = 0
    hor_lines = []
    ver_lines = []
    diag_lines = []

    for line in input_lines_p2:
        p1, p2 = line.split(' -> ')
        x1, y1 = list(map(int, p1.split(',')))
        x2, y2 = list(map(int, p2.split(',')))

        if x1 == x2:
            ver_lines.append((x1, y1, x2, y2))
        elif y1 == y2:
            hor_lines.append((x1, y1, x2, y2))
        else:
            diag_lines.append((x1, y1, x2, y2))

    points = set()
    counted_points = set()

    for ll in hor_lines:
        x1, y1, x2, y2 = ll

        const_coord = y1
        for x in range(min(x1, x2), max(x1, x2) + 1):
            p = (x, const_coord)
            if p in points and p not in counted_points:
                count += 1
                counted_points.add(p)
            else:
                points.add(p)

    for ll in ver_lines:
        x1, y1, x2, y2 = ll

        const_coord = x1
        for y in range(min(y1, y2), max(y1, y2) + 1):
            p = (const_coord, y)
            if p in points and p not in counted_points:
                count += 1
                counted_points.add(p)
            else:
                points.add(p)

    for ll in diag_lines:
        x1, y1, x2, y2 = ll

        x_range = list(range(min(x1, x2), max(x1, x2) + 1))
        y_range = list(range(min(y1, y2), max(y1, y2) + 1))

        if x1 < x2 and y1 > y2:
            y_range = y_range[::-1]
        elif x1 > x2 and y1 < y2:
            x_range = x_range[::-1]

        for xx, yy in zip(x_range, y_range):
            p = (xx, yy)
            if p in points and p not in counted_points:
                count += 1
                counted_points.add(p)
            else:
                points.add(p)

    return count


if __name__ == "__main__":
    puzzle_input = parse_input(day=5)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    