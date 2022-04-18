from abc import ABC
from collections import Counter
from copy import deepcopy
from dataclasses import dataclass

import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def serialize_password_policy(self):
        for line in self.puzzle_input():
            policy, letter, password = line.split(' ')

            policy = self.str_to_int(policy.split('-'))
            letter = letter.replace(':', '')

            yield policy, letter, password


class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    @verify_sample_input(expected_sample_output=2)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        correct_password_counter = 0

        for policy, letter, password in self.input_parser.serialize_password_policy():
            letter_counter = Counter(password)

            if policy[0] <= letter_counter[letter] <= policy[1]:
                correct_password_counter += 1

        return correct_password_counter

    @verify_sample_input(expected_sample_output=1)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        correct_password_counter = 0

        for policy, letter, password in self.input_parser.serialize_password_policy():
            if (password[policy[0]-1] == letter) ^ (password[policy[1]-1] == letter):
                correct_password_counter += 1

        return correct_password_counter


if __name__ == '__main__':
    puzzle = Solution(2020, 2)
    puzzle.reload_challenge_inputs()

    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()