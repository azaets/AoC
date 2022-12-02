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

        self.win_map = {
            'A': 'C',
            'B': 'A',
            'C': 'B'
        }

        self.lose_map = {
            'A': 'B',
            'B': 'C',
            'C': 'A'
        }

        self.points_map = {
            'A': 1,
            'B': 2,
            'C': 3
        }

        self.strategy_map = {
            'X': 0,
            'Y': 3,
            'Z': 6
        }

    @verify_sample_input(expected_sample_output=15)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        shape_map = {
            'A': 'X',  # Rock
            'B': 'Y',  # Paper
            'C': 'Z',  # Scissors
            'X': 'A',
            'Y': 'B',
            'Z': 'C'
        }

        score = 0

        for opponent, me in self.input_parser.split_by_line_by_char():
            me = shape_map[me]

            if opponent == me:
                # Draw
                score += 3
            elif opponent == self.win_map[me]:
                # Win
                score += 6
            elif self.win_map[opponent] == me:
                # Lose
                score += 0

            score += self.points_map[me]

        return score

    @verify_sample_input(expected_sample_output=12)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        score = 0

        for opponent, strategy in self.input_parser.split_by_line_by_char():
            score += self.strategy_map[strategy]

            if strategy == 'X':
                # Lose
                score += self.points_map[self.win_map[opponent]]
            elif strategy == 'Y':
                score += self.points_map[opponent]
            elif strategy == 'Z':
                score += self.points_map[self.lose_map[opponent]]

        return score


if __name__ == '__main__':
    puzzle = Solution(2022, 2)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()