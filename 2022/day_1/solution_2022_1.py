from abc import ABC
from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()
        

class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    @verify_sample_input(expected_sample_output=24000)
    def solution_part_1(self, sample_input=False):
        self.input_parser.set_input(sample_input=sample_input)

        max_food_val = 0

        for food in self.input_parser.split_by_empty_line():
            food_sum = sum(self.input_parser.str_to_int(food))

            if food_sum > max_food_val:
                max_food_val = food_sum

        return max_food_val

    @verify_sample_input(expected_sample_output=45000)
    def solution_part_2(self, sample_input=False):
        self.input_parser.set_input(sample_input=sample_input)

        carry_list = []

        for food in self.input_parser.split_by_empty_line():
            food_sum = sum(self.input_parser.str_to_int(food))
            carry_list.append(food_sum)

        # Sort carry list and add up top 3 values
        return sum(sorted(carry_list, reverse=True)[:3])


if __name__ == '__main__':
    puzzle = Solution(2022, 1)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()
