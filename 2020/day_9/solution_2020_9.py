from abc import ABC
from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def get_list_of_numbers(self):
        return self.str_to_int(self.puzzle_input())

class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    @staticmethod
    def number_validated(numbers_list, target):
        seen_nums = set()

        for n in numbers_list:
            diff = target - n
            if diff not in seen_nums:
                seen_nums.add(n)
            else:
                return True

        return False

    @verify_sample_input
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        nums = self.input_parser.get_list_of_numbers()

        fast_pointer = 25

        for i in range(len(nums) - fast_pointer - 1):
            preamble = nums[i:i+fast_pointer]
            target = nums[i + fast_pointer]
            if not self.number_validated(preamble, target):
                return nums[i + fast_pointer]

    @verify_sample_input(expected_sample_output=None)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)
        
        return 0


if __name__ == '__main__':
    puzzle = Solution(2020, 9)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()