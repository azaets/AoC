import os
import datetime
import requests


def parse_input(day, dtype=None):
    file_path = os.path.join('inputs', f'day-{day}.input')
    if os.path.exists(file_path):
        with open(file_path, 'r+') as f:
            lines = f.readlines()
            if lines:
                input_lines = [ln.strip() for ln in lines]
            else:
                input_lines = [ln.strip() for ln in download_input(day)]
                f.write('\n'.join(input_lines))
    else:
        input_lines = [ln.strip() for ln in download_input(day)]
        create_file(file_path, contents='\n'.join(input_lines))

    if dtype is int:
        input_lines = list(map(int, input_lines))

    return input_lines


def create_file(file_path, contents=''):
    try:
        with open(file_path, 'x') as f:
            f.write(contents)
    except FileExistsError:
        print("ERROR: file {py_file_path} already exists. Skipping to avoid file overwrite.")


def create_py_file_from_template(challenge_day):
    template = f"""from res.utils import parse_input, list_str_to_int
from copy import deepcopy
import numpy as np


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
    puzzle_input = parse_input(day={challenge_day})

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    """

    py_file_path = os.path.join('../2021', f'day-{challenge_day}.py')
    create_file(py_file_path, contents=template)

    # input_file_path = os.path.join('../2021/inputs', f'day-{challenge_day}.input')
    # create_file(input_file_path)


def download_input(challenge_day):
    with open('../res/aoc_session.txt', 'r') as f:
        session_id = f.readlines()[0]
    r = requests.get(f"https://adventofcode.com/2021/day/{challenge_day}/input", cookies={'session': session_id})
    return r.text.splitlines()


def list_str_to_int(list_of_str):
    return list(map(int, list_of_str))


if __name__ == "__main__":
    create_py_file_from_template(7)

