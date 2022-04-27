from abc import abstractmethod
from pathlib import Path
import logging
import requests
import webbrowser

from aoc_tools.exceptions import FailedToGetChallengeInput
from aoc_tools.parser import Parser
from aoc_tools.defenitions import PROJECT_ROOT_DIR
from aoc_tools.utils import create_file, create_solution_file_from_template

logger = logging.getLogger("AoC-Tools")


class Challenge:
    def __init__(self, year: int, day: int):
        if not (2015 <= year <= 2022):
            raise ValueError("Year must be between 2015 and 2022")
        if not (1 <= day <= 25):
            raise ValueError("Day must be between 1 and 25")

        self.year = year
        self.day = day

        self.challenge_url = f"https://adventofcode.com/{self.year}/day/{self.day}"

        self.solution_file_path = PROJECT_ROOT_DIR / Path(f"{self.year}/day_{self.day}/solution_{self.year}_{self.day}.py")
        self.input_file_path = PROJECT_ROOT_DIR / Path(f"{self.year}/day_{self.day}/input_{self.year}_{self.day}.txt")
        self.sample_input_file_path = PROJECT_ROOT_DIR / Path(f"{self.year}/day_{self.day}/sample_input_{self.year}_{self.day}.txt")

        self.session = None
        self.challenge_input = None
        self.sample_input = None

        self.input_parser: Parser = None

    def __repr__(self):
        return f"Challenge({self.year}, {self.day})"

    def __str__(self):
        return f'Advent of Code {self.year} (day {self.day})'

    @classmethod
    def init_new_challenge(cls, year: int, day: int):
        logger.info("Creating new challenge...")
        new_challenge = cls(year, day)
        new_challenge.quick_start()

    @abstractmethod
    def solution_part_1(self):
        raise NotImplementedError

    @abstractmethod
    def solution_part_2(self):
        raise NotImplementedError

    def quick_start(self):
        self.create_new_solution_template()
        self.reload_challenge_inputs()
        self.add_sample_input()
        self.open_challenge_web_page()

    def open_challenge_web_page(self):
        logger.info("Opening challenge web page...")
        webbrowser.open(self.challenge_url, new=0, autoraise=True)

    def request_challenge_input(self):
        logger.info("Retrieving challenge input...")

        challenge_input_url = f"{self.challenge_url}/input"

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
                response = self.session.get(challenge_input_url)
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

    def reload_challenge_inputs(self, reload=False):
        # Reload challenge input
        if not self.input_file_path.exists() or reload:
            self.request_challenge_input()
        else:
            with open(self.input_file_path, 'r') as input_file:
                self.challenge_input = input_file.read().splitlines()

        # Try to reload sample input
        try:
            with open(self.sample_input_file_path, 'r') as sample_input_file:
                self.sample_input = sample_input_file.read().splitlines()
        except(FileNotFoundError, IsADirectoryError):
            logger.error(f"Sample input file not found: {self.sample_input_file_path.absolute()}")

    def puzzle_input(self, sample_input=False):
        if sample_input:
            if not self.sample_input:
                raise FailedToGetChallengeInput(f"Sample input not found in file: {self.sample_input_file_path.absolute()}")
            else:
                return self.sample_input
        else:
            return self.challenge_input

    def register_input_parser(self, parser: Parser):
        self.input_parser = parser
        self.input_parser.load_inputs(challenge_input=self.puzzle_input(sample_input=False),
                                      sample_input=self.puzzle_input(sample_input=True))

    def add_sample_input(self, sample_input=None):
        logger.info("Creating file for sample input...")

        create_file(file_path=self.sample_input_file_path, contents=sample_input or "")

    def create_new_solution_template(self):
        logger.info("Creating new solution template...")
        create_solution_file_from_template(challenge_year=self.year, challenge_day=self.day)


if __name__ == "__main__":
    Challenge.init_new_challenge(2020, 9)
