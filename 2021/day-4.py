from res.utils import parse_input, list_str_to_int
from copy import deepcopy
import numpy as np


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)

    boards = []
    board = []

    numbers_drawn = input_lines_p1.pop(0)
    numbers_drawn = list_str_to_int(numbers_drawn.split(','))

    input_lines_p1.append('')

    for line in input_lines_p1:
        if not line:
            if board:
                board_and_trans = np.concatenate((np.array(board), np.transpose(np.array(board))), axis=0)
                boards.append(board_and_trans)
                board = []
        else:
            board.append(list_str_to_int(line.replace('  ', ' ').split(' ')))

    drawn_numbers = numbers_drawn[:4]
    drawn_numbers = set(drawn_numbers)

    for num in numbers_drawn[4:]:
        drawn_numbers.add(num)
        for b in boards:
            for row in b:
                count = 0
                marked_nums = []
                for n in row:
                    if n in drawn_numbers:
                        count += 1
                if count == 5:
                    for nn in drawn_numbers:
                        if nn in b[:5]:
                            marked_nums.append(nn)
                    return (np.sum(b[:5]) - sum(marked_nums)) * num


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)

    boards = []
    board = []
    numbers_drawn = input_lines_p2.pop(0)
    numbers_drawn = list(map(int, numbers_drawn.split(',')))

    input_lines_p2.append('')

    for line in input_lines_p2:
        if not line:
            if board:
                board_and_trans = np.concatenate((np.array(board), np.transpose(np.array(board))), axis=0)
                boards.append(board_and_trans)
                board = []
        else:
            board.append(list(map(int, line.replace('  ', ' ').split(' '))))

    drawn_numbers = numbers_drawn[:4]
    drawn_numbers = set(drawn_numbers)

    won_boards = []

    for num in numbers_drawn[4:]:
        drawn_numbers.add(num)
        for b in boards:
            if np.array2string(b) in won_boards:
                continue
            for row in b:
                count = 0
                marked_nums = []
                for n in row:
                    if n in drawn_numbers:
                        count += 1
                if count == 5:
                    if len(won_boards)+1 == len(boards):
                        for nn in drawn_numbers:
                            if nn in b[:5]:
                                marked_nums.append(nn)
                        return (np.sum(b[:5]) - sum(marked_nums)) * num
                    else:
                        won_boards.append(np.array2string(b))
                        break


if __name__ == "__main__":
    puzzle_input = parse_input(day=4)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    