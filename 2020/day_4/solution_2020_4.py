from abc import ABC
from copy import deepcopy
import numpy as np
import re

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def get_passport_fields(self):
        passports = list()

        for passport_fields in self.split_by_empty_line():
            fields = {field: value for field, value in [fields.split(':') for fields in passport_fields]}
            passports.append(fields)

        return passports


class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    @verify_sample_input(expected_sample_output=2)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        passport_fields = self.input_parser.get_passport_fields()
        correct_field_count = 0

        for fields in passport_fields:
            if len(fields.keys()) == 8 or (len(fields.keys()) == 7 and "cid" not in fields):
                correct_field_count += 1

        return correct_field_count

    @verify_sample_input(expected_sample_output=2)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        passport_fields = self.input_parser.get_passport_fields()
        correct_passport_count = 0

        field_validated = {
            "byr": lambda val: 1920 <= int(val) <= 2002,
            "iyr": lambda val: 2010 <= int(val) <= 2020,
            "eyr": lambda val: 2020 <= int(val) <= 2030,
            "hgt": lambda val: 150 <= int(val[:-2]) <= 193 if "cm" in val else 59 <= int(val[:-2]) <= 76,
            "hcl": lambda val: re.fullmatch(r"^#[\da-f]{6}$", val) is not None,
            "ecl": lambda val: val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
            "pid": lambda val: re.fullmatch(r"^\d{9}$", val) is not None,
            "cid": lambda val: True
        }

        for fields in passport_fields:
            if len(fields.keys()) == 8 or (len(fields.keys()) == 7 and "cid" not in fields):
                passport_correct = True
                for field, value in fields.items():
                    if not field_validated[field](value):
                        passport_correct = False
                        break

                correct_passport_count += int(passport_correct)

        return correct_passport_count


if __name__ == '__main__':
    puzzle = Solution(2020, 4)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()