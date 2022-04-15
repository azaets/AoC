import re
from collections import Counter
import itertools
from copy import deepcopy

def merge_images(img_a, img_b):
    pass


def part_2(data):
    tiles = dict()

    current_tile = 0
    for l in data:
        if l[:4] == 'Tile':
            current_tile = int(l[-5:-1])
            tiles[current_tile] = list()
        elif l == '':
            continue
        else:
            tiles[current_tile].append(l)

    borders = dict()
    img_pairs = dict()

    for t in tiles:
        top_edge = [tiles[t][0], 'top_edge']
        top_edge_inv = [tiles[t][0][::-1], 'top_edge_inv']
        botom_edge = [tiles[t][-1], 'top_edge_inv']
        botom_edge_inv = [tiles[t][-1][::-1], 'botom_edge_inv']

        left_edge = ['', 'left_edge']
        right_edge = ['', 'right_edge']

        for b in tiles[t]:
            left_edge[0] += b[0]
            right_edge[0] += b[-1]

        left_edge_inv = [left_edge[0][::-1], 'left_edge_inv']
        right_edge_inv = [right_edge[0][::-1], 'right_edge_inv']

        for e in [top_edge,
                  botom_edge,
                  top_edge_inv,
                  botom_edge_inv,
                  left_edge,
                  right_edge,
                  left_edge_inv,
                  right_edge_inv]:
            if e[0] not in borders:
                borders[e[0]] = {t: e[1]}
            else:
                borders[e[0]][t] = e[1]

                # img_pairs[e[0]] = (borders[e[0]], (t, e[1]))

    to_be_removed = []
    for b in borders:
        if len(borders[b]) < 2:
            to_be_removed.append(b)
    for r in to_be_removed:
        borders.pop(r)

    to_be_removed = []
    for b in borders:
        if 1951 in borders[b]:
            print(borders[b])

    return borders


def part_1(data):
    # print(len(data[1]))

    tiles = dict()

    current_tile = 0
    for l in data:
        if l[:4] == 'Tile':
            current_tile = int(l[-5:-1])
            tiles[current_tile] = list()
        elif l == '':
            continue
        else:
            tiles[current_tile].append(l)

    borders = dict()

    for t in tiles:
        top_edge = tiles[t][0]
        top_edge_inv = tiles[t][0][::-1]
        botom_edge = tiles[t][-1]
        botom_edge_inv = tiles[t][-1][::-1]

        left_edge = ''
        right_edge = ''

        for b in tiles[t]:
            left_edge += b[0]
            right_edge += b[-1]

        left_edge_inv = left_edge[::-1]
        right_edge_inv = right_edge[::-1]

        for e in [top_edge,
                  botom_edge,
                  top_edge_inv,
                  botom_edge_inv,
                  left_edge,
                  right_edge,
                  left_edge_inv,
                  right_edge_inv]:
            if e not in borders:
                borders[e] = [t]
            else:
                borders[e].append(t)

    filter = set()
    out = dict()

    for b in borders:
        id = borders[b]
        if len(id) > 1:
            if str(id) not in filter:
                filter.add(str(id))
                for i in id:
                    if i in out:
                        out[i] += 1
                    else:
                        out[i] = 1

    result = 1

    for o in out:
        if out[o] == 2:
            result *= o

    print(filter)
    print(out)


    return result


if __name__ == '__main__':
    with open('input/20.txt') as f:
        _lines = [_ for _ in f.read().splitlines()]

    # print(part_1(_lines))
    print(part_2(_lines))