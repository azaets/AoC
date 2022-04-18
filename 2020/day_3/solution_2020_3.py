from abc import ABC
from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def lines_to_np_array(self):
        arr = list()
        for line in self.puzzle_input():
            arr.append(list(line))
        return np.array(arr)
        

class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    @verify_sample_input(expected_sample_output=7)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        tree_grid = self.input_parser.lines_to_np_array()

        tree_counter = 0
        steps_right = 0

        for row in tree_grid[1:]:
            steps_right = (steps_right + 3) % tree_grid.shape[1]
            if row[steps_right] == '#':
                tree_counter += 1

        return tree_counter

    @verify_sample_input(expected_sample_output=336)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        tree_grid = self.input_parser.lines_to_np_array()
        out = 1

        slopes = [
            [1, 1],
            [3, 1],
            [5, 1],
            [7, 1],
            [1, 2],
        ]

        for right, down in slopes:
            steps_right = right
            steps_down = down
            tree_counter = 0

            while steps_down < tree_grid.shape[0]:
                if tree_grid[steps_down][steps_right] == '#':
                    tree_counter += 1

                steps_right = (steps_right + right) % tree_grid.shape[1]
                steps_down += down
            out *= tree_counter

        return out


if __name__ == '__main__':
    puzzle = Solution(2020, 3)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()