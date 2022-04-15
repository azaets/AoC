from res.utils import parse_input, list_str_to_int
from copy import deepcopy
from collections import Counter


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)
    
    day_count = 0
    counters = list_str_to_int(input_lines_p1[0].split(','))
    next_gen_counters = []

    while day_count < 80:
        for c in counters:
            if c == 0:
                next_gen_counters.append(6)
                next_gen_counters.append(8)
            else:
                next_gen_counters.append(c-1)

        counters = deepcopy(next_gen_counters)
        next_gen_counters = []
        day_count += 1

    return len(counters)


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)
    
    day_count = 0
    counters = list_str_to_int(input_lines_p2[0].split(','))
    fish_counter = {i: 0 for i in range(9)}

    fish_counter.update(Counter(counters))

    while day_count < 256:
        day_zero = fish_counter[0]
        for i in range(8):
            fish_counter[i] = fish_counter[i+1]

        fish_counter[8] = day_zero
        fish_counter[6] += day_zero

        day_count += 1

    return sum(fish_counter.values())


if __name__ == "__main__":
    puzzle_input = parse_input(day=6)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    