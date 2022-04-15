from collections import Counter

from res.utils import parse_input, list_str_to_int
from copy import deepcopy
import numpy as np

close_to_open_bracket_map = {
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<'
}


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    stack = []
    corrupted_brackets = []

    for line in input_lines_p1:
        for bracket in line:
            if bracket in close_to_open_bracket_map:
                open_bracket = stack.pop()
                if open_bracket != close_to_open_bracket_map[bracket]:
                    corrupted_brackets.append(bracket)
                    break
            else:
                stack.append(bracket)

    occurrences = Counter(corrupted_brackets)
    syntax_error_score = 0

    for k, v in occurrences.items():
        syntax_error_score += v * points[k]

    return syntax_error_score


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)

    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    incomplete_lines = []
    stack = []
    for line in input_lines_p2:
        for bracket in line:
            if bracket in close_to_open_bracket_map:
                open_bracket = stack.pop()
                if open_bracket != close_to_open_bracket_map[bracket]:
                    stack = []
                    break
            else:
                stack.append(bracket)

        if stack:
            incomplete_lines.append(stack)
            stack = []

    scores = []
    for line in incomplete_lines:
        score = 0
        for bracket in line[::-1]:
            score *= 5
            score += points[bracket]
        scores.append(score)

    return sorted(scores)[len(scores)//2]


if __name__ == "__main__":
    puzzle_input = parse_input(day=10)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    