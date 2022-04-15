from copy import deepcopy

def range_for(idx, _set):
    return range(min(p[idx] for p in _set) - 1, max(p[idx] for p in _set) + 2)

def part_2(data):
    ON = set()

    for r_idx, r in enumerate(data):
        for c_idx, c in enumerate(r):
            if c == '#':
                ON.add((r_idx, c_idx, 0, 0))

    radius = [-1, 0, 1]

    for _ in range(6):
        NEW_ON = set()

        for x in range_for(0, ON):
            for y in range_for(1, ON):
                for z in range_for(2, ON):
                    for w in range_for(3, ON):

                        active_n = 0

                        for dx in radius:
                            for dy in radius:
                                for dz in radius:
                                    for dw in radius:

                                        if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                            if (x + dx, y + dy, z + dz, w + dw) in ON:
                                                active_n += 1

                        if (x, y, z, w) not in ON and active_n == 3:
                            NEW_ON.add((x, y, z, w))
                        if (x, y, z, w) in ON and active_n in [2, 3]:
                            NEW_ON.add((x, y, z, w))

        ON = deepcopy(NEW_ON)

    return len(ON)



def part_1(data):

    ON = set()

    for r_idx, r in enumerate(data):
        for c_idx, c in enumerate(r):
            if c == '#':
                ON.add((r_idx, c_idx, 0))

    radius = [-1, 0, 1]

    for _ in range(6):
        NEW_ON = set()

        for x in range(-15, 15):
            for y in range(-15, 15):
                for z in range(-15, 15):
                    active_n = 0
                    for dx in radius:
                        for dy in radius:
                            for dz in radius:
                                zz = z + dz
                                yy = y + dy
                                xx = z + dx
                                if dx != 0 or dy != 0 or dz != 0:
                                    if (x + dx, y + dy, z + dz) in ON:
                                        active_n += 1

                    if ((x, y, z) not in ON) and active_n == 3:
                        NEW_ON.add((x, y, z))
                    if ((x, y, z) in ON) and active_n in [2, 3]:
                        NEW_ON.add((x, y, z))

        ON = deepcopy(NEW_ON)

    return len(ON)


    # init_space = len(data)
    #
    # space = [[['.' for _ in range(init_space)] for _ in range(init_space)] for _ in range(init_space)]
    # space[1] = [[i for i in j] for j in data]
    #
    # for i in range(init_space):
    #     for j in range(init_space):
    #         space[i][j] = ['.' for _ in range(6-1)] + space[i][j] + ['.' for _ in range(6-1)]
    #
    # for i in range(init_space):
    #     space[i] = [['.' for x in range(init_space + 2*(6-1))] for y in range(6-1)] + space[i] + [['.' for x in range(init_space + 2*(6-1))] for y in range(6-1)]
    #
    # space = [space[0] for _ in range (6-1)] + space + [space[0] for _ in range (6-1)]
    #
    # from copy import deepcopy
    #
    # temp_space = deepcopy(space)
    # boundary = len(space)
    # radius = [-1, 0, 1]
    #
    # for _ in range(6):
    #
    #     for z in range(boundary):
    #         for y in range(boundary):
    #             for x in range(boundary):
    #
    #                 active_n = 0
    #
    #                 for dz in radius:
    #                     for dy in radius:
    #                         for dx in radius:
    #                             zz = z + dz
    #                             yy = y + dy
    #                             xx = z + dx
    #                             if 0 <= zz < boundary and 0 <= yy < boundary and 0 <= xx < boundary:
    #                                 if z != 0 or y != 0 or x != 0:
    #                                     if space[zz][yy][xx] == '#':
    #                                         active_n += 1
    #
    #                 if space[z][y][x] == '#':
    #                     if not (2 <= active_n <= 3):
    #                         temp_space[z][y][x] = '.'
    #                     else:
    #                         temp_space[z][y][x] = space[z][y][x]
    #
    #                 elif space[z][y][x] == '.':
    #                     if active_n == 3:
    #                         temp_space[z][y][x] = '#'
    #                     else:
    #                         temp_space[z][y][x] = space[z][y][x]
    #
    #     space = deepcopy(temp_space)
    #
    # out = 0
    # for z in range(boundary):
    #     for y in range(boundary):
    #         for x in range(boundary):
    #             if space[z][y][x] == '#':
    #                 out += 1
    #
    # return out


if __name__ == '__main__':
    with open('input/17.txt') as f:
        _lines = [_ for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))