from pathlib import Path
import logging
import requests

from aoc_tools.defenitions import PROJECT_ROOT_DIR

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

        self.session = None

        self.challenge_input = None

    def __repr__(self):
        return f"Challenge({self.year}, {self.day})"

    def __str__(self):
        return f'Advent of Code {self.year} (day {self.day})'

    def request_challenge_input(self):
        challenge_url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'
        secret_file_path = PROJECT_ROOT_DIR / Path("res/aoc_session.txt")

        # Cookie session must be stored in a file located at project_root/res/aoc_session.txt
        if not secret_file_path.exists():
            raise FailedToGetChallengeInput("Secret file not found",
                                            "Cookie session must be stored in a file located at "
                                            "project_root/res/aoc_session.txt")

        with open(secret_file_path, 'r') as secret_file:
            if self.session is None:
                self.session = requests.Session()
                self.session.cookies.update({"session": secret_file.read().strip()})

            try:
                response = self.session.get(challenge_url)
                response.raise_for_status()
                self.challenge_input = response.text.splitlines()
            except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
                logger.error(f"Error while getting challenge input for {self}: {e}")
                raise FailedToGetChallengeInput

            input_file_path = PROJECT_ROOT_DIR / Path(f"{self.year}/input/day{self.day}.txt")

            if not Path(input_file_path).exists():
                Path(input_file_path).parent.mkdir(parents=True, exist_ok=True)

            try:
                with open(input_file_path, 'x') as input_file:
                    input_file.write('\n'.join(self.challenge_input))
            except FileExistsError:
                logger.warning(f"File already exists. Skipping to avoid file overwrite: {input_file_path}")

    def load_challenge_input(self, reload=False):
        if (self.challenge_input is None) or reload:
            self.request_challenge_input()
        else:
            input_file_path = PROJECT_ROOT_DIR / Path(f"{self.year}/input/day{self.day}.txt")
            with open(input_file_path, 'r') as input_file:
                self.challenge_input = input_file.readlines()

    def register_parser(self, parser):
        raise NotImplementedError


if __name__ == "__main__":
    challenge = Challenge(2020, 6)
    challenge.load_challenge_input()
