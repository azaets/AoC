from pathlib import Path
import logging
import requests

from aoc_tools.defenitions import PROJECT_ROOT_DIR
from aoc_tools.utils import create_file

logger = logging.getLogger("AoC-Tools")


class FailedToGetChallengeInput(Exception):
    """ Unexpected error during request for challenge input. """


class Challenge:
    def __init__(self, year: int, day: int):
        if not (2015 <= year <= 2022):
            raise ValueError("Year must be between 2015 and 2022")
        if not (1 <= day <= 25):
            raise ValueError("Day must be between 1 and 25")

        self.year = year
        self.day = day

        self.input_file_path = PROJECT_ROOT_DIR / Path(f"{self.year}/day_{self.day}/input_{self.year}_{self.day}.txt")

        self.session = None

        self.challenge_input = None

    def __repr__(self):
        return f"Challenge({self.year}, {self.day})"

    def __str__(self):
        return f'Advent of Code {self.year} (day {self.day})'

    def request_challenge_input(self):
        challenge_url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'

        # Cookie session must be stored in a file located at project_root/res/aoc_session.txt
        secret_file_path = PROJECT_ROOT_DIR / Path("res/aoc_session.txt")
        if not secret_file_path.exists():
            raise FailedToGetChallengeInput("Secret file not found",
                                            "Cookie session must be stored in a file located at "
                                            "project_root/res/aoc_session.txt")

        with open(secret_file_path, 'r') as secret_file:
            # Create a new http session with cookie secret
            if self.session is None:
                self.session = requests.Session()
                self.session.cookies.update({"session": secret_file.read().strip()})

            # Download challenge input
            try:
                response = self.session.get(challenge_url)
                response.raise_for_status()
                self.challenge_input = response.text.splitlines()

            except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
                logger.error(f"Error while getting challenge input for {self}: {e}")
                raise FailedToGetChallengeInput

            # Save challenge input to file
            try:
                create_file(self.input_file_path, '\n'.join(self.challenge_input))
                logger.debug(f"Challenge input for {self} saved to {self.input_file_path}")
            except FileExistsError:
                logger.debug(f"File already exists. Skipping to avoid file overwrite: {self.input_file_path}")

    def get_challenge_input(self, reload=False):
        if (self.challenge_input is None) or reload:
            self.request_challenge_input()
        else:
            with open(self.input_file_path, 'r') as input_file:
                self.challenge_input = input_file.readlines()

        return self.challenge_input

    def register_parser(self, parser):
        raise NotImplementedError


if __name__ == "__main__":
    challenge = Challenge(2020, 6)
    challenge.get_challenge_input()
