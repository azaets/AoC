from res.utils import parse_input, list_str_to_int
from copy import deepcopy
import numpy as np


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)
    count = 0

    for line in input_lines_p1:
        sig_patterns, digit_output = line.split(' | ')
        segment_count_to_digit = {
            2: 1,
            3: 7,
            4: 4,
            7: 8
        }

        for digit in digit_output.split(' '):
            if len(digit) in segment_count_to_digit:
                count += 1

    return count


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)
    
    count = 0

    segment_count_to_digit = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    segments_map = {letter: '' for letter in 'abcdefg'}

    for line in input_lines_p2:
        sig_patterns, digit_output = line.split(' | ')
        combined = sig_patterns.split(' ') + digit_output.split(' ')

        nums = dict()

        for pattern in combined:
            if len(pattern) in segment_count_to_digit:
                nums[segment_count_to_digit[len(pattern)]] = set(pattern)

        segments_map['a'] = nums[7] - nums[1]

        for pattern in combined:
            pattern_set = set(pattern)
            if len(pattern_set) > 5:
                if len(pattern_set - set.union(nums[4], segments_map['a'])) == 1:
                    segments_map['g'] = pattern_set - set.union(nums[4], segments_map['a'])
                    nums[9] = pattern_set
                    break

        segments_map['e'] = nums[8] - nums[9]

        for pattern in combined:
            pattern_set = set(pattern)
            if len(pattern_set) == 6:
                if len(pattern_set - nums[1] - segments_map['a'] - segments_map['e'] - segments_map['g']) == 1:
                    segments_map['b'] = pattern_set - nums[1] - segments_map['a'] - segments_map['e'] - segments_map['g']
                    nums[0] = pattern_set
                    break

        for pattern in combined:
            pattern_set = set(pattern)
            if len(pattern_set) == 7:
                if len(pattern_set - nums[0]) == 1:
                    segments_map['d'] = pattern_set - nums[0]
                    break

        for pattern in combined:
            pattern_set = set(pattern)
            if len(pattern_set) == 6:
                if len(pattern_set - segments_map['a'] - segments_map['b'] - segments_map['d'] - segments_map['e'] - segments_map['g']) == 1:
                    segments_map['f'] = pattern_set - segments_map['a'] - segments_map['b'] - segments_map['d'] - segments_map['e'] - segments_map['g']
                    break

        segments_map['c'] = nums[1] - segments_map['f']

        nums[0] = nums[8] - segments_map['d']
        nums[2] = nums[8] - segments_map['f'] - segments_map['b']
        nums[3] = nums[8] - segments_map['b'] - segments_map['e']
        nums[5] = nums[8] - segments_map['c'] - segments_map['e']
        nums[6] = nums[8] - segments_map['c']

        maper = {''.join(sorted(v)): str(k) for k, v in nums.items()}

        out_numb = ''
        for digit in digit_output.split(' '):
            if ''.join(sorted(digit)) in maper:
                out_numb += maper[''.join(sorted(digit))]

        count += int(out_numb)

    return count


if __name__ == "__main__":
    puzzle_input = parse_input(day=8)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    