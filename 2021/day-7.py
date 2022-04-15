from res.utils import parse_input, list_str_to_int
from copy import deepcopy
import numpy as np


def find_sum_of_deltas(positions, target):
    sum_deltas = 0
    for p in positions:
        sum_deltas += abs(target - p)

    return sum_deltas


def find_sum_of_dynamic_deltas(positions, target):
    sum_deltas = 0
    for p in positions:
        steps = abs(target - p)
        cost = steps * (steps + 1) // 2
        sum_deltas += cost

    return sum_deltas


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)

    positions = list_str_to_int(input_lines_p1[0].split(','))

    # fuel_cost = min([find_sum_of_deltas(positions, i) for i in range(min(positions), max(positions))])

    """ UPD: Optimization for O(1) memory  """
    floor, ceiling = min(positions), max(positions)
    fuel_cost = None

    for target in range(floor, ceiling + 1):
        target_cost = 0
        for position in positions:
            target_cost += abs(target - position)

        if fuel_cost is None:
            fuel_cost = target_cost
        else:
            fuel_cost = min(fuel_cost, target_cost)

    return fuel_cost


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)

    positions = list_str_to_int(input_lines_p2[0].split(','))

    # fuel_cost = min([find_sum_of_dynamic_deltas(positions, i) for i in range(min(positions), max(positions))])

    """ UPD: Optimization for O(1) memory  """
    floor, ceiling = min(positions), max(positions)
    fuel_cost = None

    for target in range(floor, ceiling + 1):
        target_cost = 0
        for position in positions:
            steps = abs(target - position)
            cost = steps * (steps + 1) // 2
            target_cost += cost

        if fuel_cost is None:
            fuel_cost = target_cost
        else:
            fuel_cost = min(fuel_cost, target_cost)

    return fuel_cost


if __name__ == "__main__":
    puzzle_input = parse_input(day=7)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
