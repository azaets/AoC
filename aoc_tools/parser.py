import logging
from typing import List

from aoc_tools.exceptions import FailedToGetChallengeInput

logger = logging.getLogger("AoC-Tools")


class Parser:
    def __init__(self):
        self.challenge_input = None
        self.sample_input = None

        self.input_selector = 'challenge'

    def load_inputs(self, challenge_input, sample_input):
        self.challenge_input = challenge_input
        self.sample_input = sample_input

    def puzzle_input(self):
        if self.input_selector == "sample":
            if not self.sample_input:
                raise FailedToGetChallengeInput(f"Sample input not found")
            else:
                return self.sample_input
        elif self.input_selector == "challenge":
            return self.challenge_input

    def set_input(self, sample_input):
        if sample_input:
            self.input_selector = "sample"
        else:
            self.input_selector = "challenge"

    # Helper Functions

    def split_by_empty_line(self):
        line_group = list()
        for line in self.puzzle_input():
            if not line:
                yield line_group
                line_group = list()
            else:
                line_group.extend(line.split(' '))

        yield line_group  # Yield the last group of lines

    def split_by_line_by_char(self):
        for line in self.puzzle_input():
            yield line.split()

    def str_to_int(self, list_of_str: List[str]) -> List[int]:
        return list(map(int, list_of_str))
