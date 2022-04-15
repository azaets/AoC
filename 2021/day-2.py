from res.utils import parse_input


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')

    depth = 0
    fwd = 0

    for instruction in input_lines:
        direction, magnitude = instruction.split()

        if direction == 'up':
            depth -= int(magnitude)
        elif direction == 'down':
            depth += int(magnitude)
        elif direction == 'forward':
            fwd += int(magnitude)

    return depth * fwd


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    aim = 0
    depth = 0
    fwd = 0

    for instruction in input_lines:
        direction, magnitude = instruction.split()

        if direction == 'up':
            aim -= int(magnitude)
        elif direction == 'down':
            aim += int(magnitude)
        elif direction == 'forward':
            fwd += int(magnitude)
            depth += int(magnitude) * aim

    return depth * fwd


if __name__ == "__main__":
    puzzle_input = parse_input(day=2)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    