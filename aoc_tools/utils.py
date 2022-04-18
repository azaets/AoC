import logging
from pathlib import Path
from functools import wraps

from aoc_tools.defenitions import PROJECT_ROOT_DIR


logger = logging.getLogger("AoC-Tools")


def display_return_value(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            print(f"{func.__name__}: {result}")
        return result
    return wrapper


def verify_sample_input(original_function=None, expected_sample_output=None):
    def _decorate(function):
        @wraps(function)
        def wrapped_function(*args, **kwargs):
            if expected_sample_output:
                result = function(*args, sample_input=True)
                if result != expected_sample_output:
                    logger.warning(f"{function.__name__} | Produced result of {result} does not match expected output of {expected_sample_output}")
                    return result
                else:
                    logger.info(f"{function.__name__} | Successfully passed test case. Result: {result}")
                    result = function(*args, sample_input=False)
                    logger.info(f"{function.__name__} | Challenge output: {result}")
                    return result
            else:
                return function(*args, sample_input=False)
        return wrapped_function

    if original_function:
        return _decorate(original_function)
    return _decorate


def create_file(file_path, contents):
    """
    Create file with given contents.
    :param file_path: Path to file.
    :param contents: Contents of the file.
    :return: None
    """
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'x') as f:
            f.write(contents)
    else:
        logger.warning(f"File {file_path} already exists.")


def create_solution_file_from_template(challenge_year, challenge_day):
    template = f"""
    
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

    @verify_sample_input(expected_sample_output=None)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        return 0

    @verify_sample_input(expected_sample_output=None)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)
        
        return 0


if __name__ == '__main__':
    puzzle = Solution({challenge_year}, {challenge_day})
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()
    
"""

    py_file_path = PROJECT_ROOT_DIR / Path(f"{challenge_year}/day_{challenge_day}/solution_{challenge_year}_{challenge_day}.py")
    create_file(py_file_path, contents=template.strip())


if __name__ == "__main__":
    create_solution_file_from_template(challenge_year=2020, challenge_day=1)
