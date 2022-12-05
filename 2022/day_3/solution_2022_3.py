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

    @verify_sample_input(expected_sample_output=157)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        out = 0

        for rucksack in self.input_parser.puzzle_input():
            rucksack = list(rucksack)
            comp1 = rucksack[:len(rucksack)//2]
            comp2 = rucksack[len(rucksack)//2:]
            intersect = set(comp2).intersection(set(comp1))

            item = intersect.pop()
            priority = ord(item)-96
            if priority < 0:
                priority += 58
            out += priority

        return out

    @verify_sample_input(expected_sample_output=70)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        out = 0
        set_group = []

        for rucksack in self.input_parser.puzzle_input():
            set_group.append(set(rucksack))
            if len(set_group) == 3:
                intersect = reduce(lambda x, y: x & y, set_group)

                item = intersect.pop()
                priority = ord(item) - 96

                if priority < 0:
                    priority += 58
                out += priority
                set_group = []

        return out


if __name__ == '__main__':
    puzzle = Solution(2022, 3)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()