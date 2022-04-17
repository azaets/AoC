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


class Day{challenge_day}(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)

    def solution_part_1(self):
        print(self.challenge_input)

    def solution_part_2(self):
        print(self.challenge_input)


if __name__ == '__main__':
    puzzle = Day{challenge_day}({challenge_year}, {challenge_day})
    puzzle.reload_challenge_input()
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()
    
"""

    py_file_path = PROJECT_ROOT_DIR / Path(f"{challenge_year}/day_{challenge_day}/solution_{challenge_year}_{challenge_day}.py")
    create_file(py_file_path, contents=template.strip())


if __name__ == "__main__":
    create_solution_file_from_template(challenge_year=2020, challenge_day=1)
