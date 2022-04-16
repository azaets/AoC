import logging
from aoc_tools.defenitions import PROJECT_ROOT_DIR


logger = logging.getLogger("AoC-Tools")


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


def create_py_file_from_template(challenge_year, challenge_day):
    template = f"""from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)

    count = 0

    return count


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)

    count = 0

    return count


if __name__ == "__main__":
    challenge = Challenge(year={challenge_year}, day={challenge_day})
    puzzle_input = challenge.get_challenge_input()

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))

    """

    py_file_path = PROJECT_ROOT_DIR / f"{challenge_year}/day_{challenge_day}/solution_{challenge_year}_{challenge_day}.py"
    create_file(py_file_path, contents=template)


if __name__ == "__main__":
    create_py_file_from_template(challenge_year=2019, challenge_day=1)
