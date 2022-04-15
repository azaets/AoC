import re
from collections import Counter, OrderedDict
import itertools
from copy import deepcopy



def part_2(data):
    directions = {'e', 'se', 'sw', 'w', 'nw', 'ne'}
    flipped_tiles = dict()
    black_tile_map = set()
    white_tile_map = set()

    for d in data:
        position = {'e': 0, 'se': 0, 'sw': 0, 'w': 0, 'nw': 0, 'ne': 0}
        i = 0
        while i < len(d):
            if d[i] in directions:
                position[d[i]] += 1
            else:
                position[d[i:i+2]] += 1
                i += 1

            i += 1

        x = 0
        y = 0

        for k, v in position.items():
            if k == 'e' and v > 0:
                x += 2 * v
            elif k == 'w' and v > 0:
                x -= 2 * v
            elif k == 'se' and v > 0:
                x += 1 * v
                y -= 1 * v
            elif k == 'sw' and v > 0:
                x -= 1 * v
                y -= 1 * v
            elif k == 'nw' and v > 0:
                x -= 1 * v
                y += 1 * v
            elif k == 'ne' and v > 0:
                x += 1 * v
                y += 1 * v

        p_str = '{},{}'.format(x,y)

        if p_str not in flipped_tiles:
            flipped_tiles[p_str] = 1
        else:
            flipped_tiles[p_str] += 1

    for k, v in flipped_tiles.items():
        if v % 2 != 0:
            coord = [int(i) for i in k.split(',')]
            black_tile_map.add(tuple(coord))

    for _ in range(1):
        for x, y in black_tile_map:
            neighbours = 0
            for dy in [-1, 0, 1]:
                if dy == 0:
                    for dx in [-2, 2]:
                        if (x+dx, y+dy) not in black_tile_map:
                            pass
                else:
                    for dx in [-1, 1]:
                        pass

    return black_tile_map


def part_1(data):
    directions = {'e', 'se', 'sw', 'w', 'nw', 'ne'}
    flipped_tiles = dict()

    for d in data:
        position = {'e': 0, 'se': 0, 'sw': 0, 'w': 0, 'nw': 0, 'ne': 0}
        i = 0
        while i < len(d):
            if d[i] in directions:
                position[d[i]] += 1
            else:
                position[d[i:i+2]] += 1
                i += 1

            i += 1

        x = 0
        y = 0

        for k, v in position.items():
            if k == 'e' and v > 0:
                x += 2 * v
            elif k == 'w' and v > 0:
                x -= 2 * v
            elif k == 'se' and v > 0:
                x += 1 * v
                y -= 1 * v
            elif k == 'sw' and v > 0:
                x -= 1 * v
                y -= 1 * v
            elif k == 'nw' and v > 0:
                x -= 1 * v
                y += 1 * v
            elif k == 'ne' and v > 0:
                x += 1 * v
                y += 1 * v

        p_str = str((x, y))

        if p_str not in flipped_tiles:
            flipped_tiles[p_str] = 1
        else:
            flipped_tiles[p_str] += 1

    out = 0

    for v in flipped_tiles.values():
        if v % 2 != 0:
            out += 1

    return out

if __name__ == '__main__':
    with open('input/24.txt') as f:
        _lines = [_ for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))
