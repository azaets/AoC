from res.utils import parse_input, list_str_to_int
from copy import deepcopy
import numpy as np


def next_state(grid):
    count = 0

    map_x_dim, map_y_dim = grid.shape
    neighboring_cells = [-1, 0, 1]

    flashed_coords = set()
    states_to_coord = {i: set() for i in range(11)}
    coor_to_state = dict()

    """First, the energy level of each octopus increases by 1"""
    grid = grid + 1

    for y in range(map_y_dim):
        for x in range(map_x_dim):
            states_to_coord[grid[y][x]].add((x, y))
            coor_to_state[(x, y)] = grid[y][x]

    while states_to_coord[10]:
        flashing_coord = x, y = states_to_coord[10].pop()
        count += 1

        coor_to_state[flashing_coord] = 0
        states_to_coord[0].add(flashing_coord)

        flashed_coords.add(flashing_coord)

        for dx in neighboring_cells:
            if x + dx < 0 or x + dx > map_x_dim - 1:
                continue
            for dy in neighboring_cells:
                if y + dy < 0 or y + dy > map_y_dim - 1 or dx == dy == 0:
                    continue

                neighbor_coord = (x + dx, y + dy)

                current_state = coor_to_state[neighbor_coord]
                if current_state > 9 or neighbor_coord in flashed_coords:
                    continue

                states_to_coord[current_state].remove(neighbor_coord)

                coor_to_state[neighbor_coord] = current_state + 1
                states_to_coord[current_state + 1].add(neighbor_coord)

    new_grid = np.zeros(grid.shape, dtype=int)

    for coord, state in coor_to_state.items():
        x, y = coord
        new_grid[y][x] = state

    return count, new_grid


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)
    count = 0
    grid = [list_str_to_int(list(row)) for row in input_lines_p1]
    grid = np.array(grid)

    for _ in range(100):
        next_count, next_grid = next_state(grid)

        count += next_count
        grid = next_grid

    return count


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)
    count = 0
    grid = [list_str_to_int(list(row)) for row in input_lines_p2]
    grid = np.array(grid)

    while True:
        count += 1
        _, next_grid = next_state(grid)

        grid = next_grid
        states = {sum(row) for row in grid}
        if len(states) == 1:
            return count


if __name__ == "__main__":
    puzzle_input = parse_input(day=11, test_input=False)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
