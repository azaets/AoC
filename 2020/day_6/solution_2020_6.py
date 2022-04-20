from abc import ABC
from copy import deepcopy
from functools import reduce

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

    @staticmethod
    def find_intersection(set1: set, set2: set) -> set:
        return set1.intersection(set2)

    @verify_sample_input(expected_sample_output=11)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        sum_of_counts = 0

        for group in self.input_parser.split_by_empty_line():
            combined_answers = reduce(lambda l1, l2: l1 + l2, group)
            yes_answers = set(combined_answers)
            sum_of_counts += len(yes_answers)

        return sum_of_counts

    @verify_sample_input(expected_sample_output=6)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        sum_of_counts = 0

        for group in self.input_parser.split_by_empty_line():
            set_group = [set(person_answers) for person_answers in group]
            unique_answers = reduce(self.find_intersection, set_group)
            sum_of_counts += len(unique_answers)

        return sum_of_counts


if __name__ == '__main__':
    puzzle = Solution(2020, 6)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()