from functools import reduce

from res.utils import parse_input, list_str_to_int
from copy import deepcopy
import numpy as np


def find_neighbours(grid, grid_dims, coords):
    neighboring_cells = [-1, 0, 1]
    neighbors = []
    x, y = coords
    map_x_dim, map_y_dim = grid_dims

    for hor in neighboring_cells:
        if x + hor < 0 or x + hor > map_x_dim - 1:
            continue
        for ver in neighboring_cells:
            if y + ver < 0 or y + ver > map_y_dim - 1:
                continue

            if hor == ver or hor + ver == 0:
                continue

            neighbors.append(grid[y + ver][x + hor])

    return neighbors


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)

    cave_map = [list_str_to_int(list(line)) for line in input_lines_p1]
    map_x_dim, map_y_dim = np.shape(cave_map)
    local_min = []

    for y in range(map_y_dim):
        for x in range(map_x_dim):
            neighbors = find_neighbours(grid=cave_map,
                                        grid_dims=(map_x_dim, map_y_dim),
                                        coords=(x, y))

            if cave_map[y][x] < min(neighbors):
                local_min.append(cave_map[y][x])

    return sum([i+1 for i in local_min])


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)

    cave_map = [list_str_to_int(list(line)) for line in input_lines_p2]
    map_x_dim, map_y_dim = np.shape(cave_map)
    neighboring_cells = [-1, 0, 1]
    local_min = []

    for y in range(map_y_dim):
        for x in range(map_x_dim):
            neighbors = find_neighbours(grid=cave_map,
                                        grid_dims=(map_x_dim, map_y_dim),
                                        coords=(x, y))

            if cave_map[y][x] < min(neighbors):
                local_min.append((y, x))

    basin_sizes = []

    for point in local_min:
        size = 0
        visited_neighbours = set()
        next_neighbours = {point}

        while next_neighbours:
            next_neighbours_loop = set()
            for neighbor in next_neighbours:
                visited_neighbours.add(neighbor)
                y, x = neighbor
                size += 1

                for hor in neighboring_cells:
                    if x + hor < 0 or x + hor > map_x_dim - 1:
                        continue
                    for ver in neighboring_cells:
                        if y + ver < 0 or y + ver > map_y_dim - 1:
                            continue

                        if hor == ver or hor + ver == 0:
                            continue

                        if cave_map[y + ver][x + hor] == 9:
                            continue
                        elif (y + ver, x + hor) not in visited_neighbours:
                            next_neighbours_loop.add((y + ver, x + hor))

            next_neighbours = deepcopy(next_neighbours_loop)

        basin_sizes.append(size)

    return reduce(lambda i, j: i * j, sorted(basin_sizes)[-3:])


if __name__ == "__main__":
    puzzle_input = parse_input(day=9)

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    