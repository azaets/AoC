from collections import Counter
from copy import deepcopy


def find_adj_p2(data, row, col):
    adj_seats = 0

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if not (dc == 0 and dr == 0):
                r = row + dr
                c = col + dc
                while 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] == '.':
                    r += dr
                    c += dc
                if 0 <= r < len(data) and 0 <= c < len(data[0]):
                    if data[r][c] == '#':
                        adj_seats += 1
    return adj_seats


def part_2(data):

    while True:
        change = False
        new_map = deepcopy(data)
        for row in range(len(data)):
            for col in range(len(data[row])):
                adj = find_adj_p2(data, row, col)
                if adj < 5:
                    if data[row][col] == 'L' and adj == 0:
                        new_map[row][col] = '#'
                        change = True
                else:
                    if data[row][col] == '#':
                        new_map[row][col] = 'L'
                        change = True

        if change is False:
            out = 0
            for r in new_map:
                out += Counter(r)['#']
            return  out

        data = deepcopy(new_map)


def find_adj_p1(data, row, col):
    adj_seats = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if 0 <= row+dr < len(data) and 0 <= col+dc < len(data[0]) and not (dc == 0 and dr == 0):
                if data[row + dr][col + dc] == '#':
                    adj_seats += 1
    return adj_seats

def part_1(data):
    while True:
        change = False
        new_map = deepcopy(data)
        for row in range(len(data)):
            for col in range(len(data[row])):
                adj = find_adj_p1(data, row, col)
                if adj < 4:
                    if data[row][col] == 'L' and adj == 0:
                        new_map[row][col] = '#'
                        change = True
                else:
                    if data[row][col] == '#':
                        new_map[row][col] = 'L'
                        change = True

        if change is False:
            out = 0
            for r in new_map:
                out += Counter(r)['#']
            return  out

        data = deepcopy(new_map)


if __name__ == '__main__':
    with open('input/11.txt') as f:
        _lines = [list(_) for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))