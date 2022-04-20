from abc import ABC
from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def boarding_passes_as_list(self):
        return [list(boarding_pass) for boarding_pass in self.puzzle_input()]
        

class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

    def get_seat_id(self):
        boarding_passes = self.input_parser.boarding_passes_as_list()

        char_action = {
            "F": lambda val: [val[0], val[0] + (val[1] - val[0]) // 2],
            "B": lambda val: [1 + val[0] + (val[1] - val[0]) // 2, val[1]],
            "L": lambda val: [val[0], val[0] + (val[1] - val[0]) // 2],
            "R": lambda val: [1 + val[0] + (val[1] - val[0]) // 2, val[1]],
        }

        for boarding_pass in boarding_passes:
            row = [0, 127]
            col = [0, 7]
            for row_char in boarding_pass[:7]:
                row = char_action[row_char](row)

            for col_char in boarding_pass[7:]:
                col = char_action[col_char](col)

            yield row[0] * 8 + col[0]

    @verify_sample_input(expected_sample_output=357)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        max_seat_id = 0

        for seat_id in self.get_seat_id():
            max_seat_id = max(max_seat_id, seat_id)

        return max_seat_id

    @verify_sample_input
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        seat_ids = []

        for seat_id in self.get_seat_id():
            seat_ids.append(seat_id)

        sorted_seat_ids = sorted(seat_ids)

        for i, seat_id in enumerate(sorted_seat_ids, start=1):
            if sorted_seat_ids[i] - sorted_seat_ids[i-1] > 1:
                return sorted_seat_ids[i] - 1


if __name__ == '__main__':
    puzzle = Solution(2020, 5)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()