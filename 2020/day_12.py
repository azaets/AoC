from copy import deepcopy

def part_2(data):
    directions = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
    # manhatan_dist = ['E' if directions['E']-directions['W'] > 0 else 'W', 'N' if directions['N']-directions['S'] > 0 else 'S']
    # manhatan_dist = [abs(directions['E']-directions['W']), abs(directions['N']-directions['S'])]

    rotation_r = ['E', 'S', 'W', 'N']
    rotation_l = ['E', 'N', 'W', 'S']

    w_point = {'E': 10, 'S': 0, 'W': 0, 'N': 1}

    for d in data:
        w_point_dist = [abs(w_point['E'] - w_point['W']), abs(w_point['N'] - w_point['S'])]
        w_point_direction = ['E' if w_point['E'] - w_point['W'] > 0 else 'W', 'N' if w_point['N'] - w_point['S'] > 0 else 'S']
        dir = d[0]
        val = int(d[1:])
        if dir == 'F':
            directions[w_point_direction[0]] += w_point_dist[0]*val
            directions[w_point_direction[1]] += w_point_dist[1]*val
        elif dir in directions:
            w_point[dir] += val
        elif dir in {'L', 'R'}:
            if dir == 'R':
                new_w_point = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
                for r in rotation_r:
                    new_w_point[rotation_r[(rotation_r.index(r) + (val // 90)) % 4]] = w_point[r]
                w_point = deepcopy(new_w_point)
            elif dir == 'L':
                new_w_point = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
                for l in rotation_l:
                    new_w_point[rotation_l[(rotation_l.index(l) + (val // 90)) % 4]] = w_point[l]
                w_point = deepcopy(new_w_point)

    return abs(directions['E'] - directions['W']) + abs(directions['S'] - directions['N'])


def part_1(data):
    directions = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
    fwd_direction = 'E'
    rotation_r = ['E', 'S', 'W', 'N']
    rotation_l = ['E', 'N', 'W', 'S']

    for d in data:
        dir = d[0]
        val = int(d[1:])
        if dir == 'F':
            directions[fwd_direction] += val
        elif dir in directions:
            directions[dir] += val
        elif dir in {'L', 'R'}:
            if dir == 'R':
                fwd_direction = rotation_r[(rotation_r.index(fwd_direction) + (val // 90)) % 4]
            elif dir == 'L':
                fwd_direction = rotation_l[(rotation_l.index(fwd_direction) + (val // 90)) % 4]

    return abs(directions['E']-directions['W']) + abs(directions['S']-directions['N'])


if __name__ == '__main__':
    with open('input/12.txt') as f:
        _lines = [_ for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))