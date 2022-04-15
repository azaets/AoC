from res.utils import parse_input, list_str_to_int
from copy import deepcopy
import numpy as np
import heapq


def part_1(input_lines):
    print('-- Part 1 ----------------------------------')
    input_lines_p1 = deepcopy(input_lines)

    cave_map = np.array([list_str_to_int(line) for line in input_lines_p1])
    path_cost = np.full(cave_map.shape, 1e9, dtype=int)

    visited_nodes = set()
    next_queue = set()
    path_cost[(0, 0)] = 0
    next_queue.add((0, 0))

    while len(next_queue) > 0:
        queue = deepcopy(next_queue)
        next_queue = set()

        for current_node in queue:
            if current_node not in visited_nodes:
                for r in [-1, 0, 1]:
                    for c in [-1, 0, 1]:
                        if abs(r) == abs(c):
                            continue

                        row, col = current_node
                        next_node = (row + r, col + c)

                        r, c = next_node
                        if 0 <= r < cave_map.shape[0] and 0 <= c < cave_map.shape[1]:
                            if path_cost[current_node] + cave_map[next_node] < path_cost[next_node]:
                                path_cost[next_node] = path_cost[current_node] + cave_map[next_node]

                            next_queue.add(next_node)

            visited_nodes.add(current_node)

    count = path_cost[(-1, -1)]

    # print(path_cost)
    #
    # path_cost = np.full(cave_map.shape, 0, dtype=int)
    #
    # for row in range(cave_map.shape[0]):
    #     for col in range(cave_map.shape[1]):
    #         if row == 0 and col == 0:
    #             pass
    #         elif row == 0:
    #             path_cost[row][col] = cave_map[row][col] + path_cost[row][col-1]
    #         elif col == 0:
    #             path_cost[row][col] = cave_map[row][col] + path_cost[row - 1][col]
    #         else:
    #             path_cost[row][col] = cave_map[row][col] + min(path_cost[row - 1][col], path_cost[row][col - 1])
    #
    # count = path_cost[-1][-1]
    #
    # print(path_cost)

    return count


def part_2(input_lines):
    print('-- Part 2 ----------------------------------')
    input_lines_p2 = deepcopy(input_lines)
    
    count = 0

    return count


if __name__ == "__main__":
    puzzle_input = parse_input(day=15, )

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
    