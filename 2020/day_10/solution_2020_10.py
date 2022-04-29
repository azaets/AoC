from abc import ABC
from collections import defaultdict
from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def get_sorter_adapters(self):
        return sorted(self.str_to_int(self.puzzle_input()))


class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    @verify_sample_input(expected_sample_output=220)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        adapters_sorted = self.input_parser.get_sorter_adapters()

        adapters_sorted.insert(0, 0)  # Add outlet rating
        adapters_sorted.append(adapters_sorted[-1] + 3)  # Add device adapter rating

        diff_dict = defaultdict(int)
        prev_adapter_rating = adapters_sorted[0]

        for i, adapter_rating in enumerate(adapters_sorted, start=1):
            jolt_diff = adapter_rating - prev_adapter_rating
            diff_dict[jolt_diff] += 1
            prev_adapter_rating = adapter_rating

        return diff_dict[1] * diff_dict[3]

    @verify_sample_input(expected_sample_output=19208)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        return 0


if __name__ == '__main__':
    puzzle = Solution(2020, 10)
    puzzle.reload_challenge_inputs()

    parser = InputParser()
    puzzle.register_input_parser(parser)

    puzzle.solution_part_1()
    puzzle.solution_part_2()
