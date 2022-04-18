from abc import ABC
from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def convert_strs_to_nums(self):
        return self.str_to_int(self.puzzle_input())


class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    @verify_sample_input(expected_sample_output=514579)
    def solution_part_1(self, sample_input=True):
        """Classic two-sum problem"""
        self.input_parser.set_input(sample_input=sample_input)

        input_numbers = self.input_parser.convert_strs_to_nums()

        target_sum = 2020
        seen_numbers = set()

        for num in input_numbers:
            diff = target_sum - num
            if diff in seen_numbers:
                return num * diff
            else:
                seen_numbers.add(num)

    @verify_sample_input(expected_sample_output=241861950)
    def solution_part_2(self, sample_input=True):
        """ Classic three-sum problem """
        self.input_parser.set_input(sample_input=sample_input)

        input_numbers = self.input_parser.convert_strs_to_nums()

        target_sum = 2020
        first_number_diff = [target_sum - num for num in input_numbers]

        for i, temp_target in enumerate(first_number_diff):
            seen_numbers = set()
            for j, num in enumerate(input_numbers):
                if i == j:
                    continue
                diff = temp_target - num
                if diff in seen_numbers:
                    return input_numbers[i] * diff * num
                else:
                    seen_numbers.add(num)


if __name__ == '__main__':
    puzzle = Solution(2020, 1)
    puzzle.reload_challenge_inputs()

    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()
