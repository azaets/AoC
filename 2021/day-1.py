from res.utils import parse_input


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    count = 0
    prev_value = None

    for i in input_lines:
        if prev_value and prev_value < i:
            count += 1
        prev_value = i

    return count


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    count = 0
    prev_value = None
    window_size = 3

    for i in range(len(input_lines)-window_size+1):
        window_sum = sum(input_lines[i:i+window_size])
        if prev_value and prev_value < window_sum:
            count += 1
        prev_value = window_sum

    return count


if __name__ == "__main__":
    puzzle_input = parse_input(day=1, dtype=int)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    