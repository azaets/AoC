from abc import ABC
from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def split_instructions(self):
        for line in self.puzzle_input():
            yield line.split(' ')

    def create_instruction_set(self):
        return [(instr, int(val)) for instr, val in self.split_instructions()]
        

class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    @verify_sample_input(expected_sample_output=5)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        instruction_set = self.input_parser.create_instruction_set()

        accumulator = 0
        executed_instructions = set()
        program_counter = 0

        while program_counter not in executed_instructions:
            executed_instructions.add(program_counter)

            instruction, value = instruction_set[program_counter]

            if instruction == 'nop':
                program_counter += 1
            elif instruction == 'acc':
                accumulator += value
                program_counter += 1
            elif instruction == 'jmp':
                program_counter += value

        return accumulator

    @verify_sample_input(expected_sample_output=None)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)
        
        return 0


if __name__ == '__main__':
    puzzle = Solution(2020, 8)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()