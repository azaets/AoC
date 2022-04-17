from abc import ABC
from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.utils import display_return_value


class Day1(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)

        self.TEST_INPUT = True

    @display_return_value
    def solution_part_1(self):
        """Classic two-sum problem"""
        input_numbers = [int(num) for num in self.puzzle_input]

        target_sum = 2020
        seen_numbers = set()

        for num in input_numbers:
            diff = target_sum - num
            if diff in seen_numbers:
                return num * diff
            else:
                seen_numbers.add(num)

    @display_return_value
    def solution_part_2(self):
        """ Classic three-sum problem """
        input_numbers = [int(num) for num in self.puzzle_input]

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
    puzzle = Day1(2020, 1)
    puzzle.reload_challenge_inputs()
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()
