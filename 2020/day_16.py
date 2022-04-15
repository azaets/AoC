from copy import deepcopy

def part_1(data):
    notes = {'rules': [], 'ticket': [], 'n_tickets': []}
    key = 'rules'
    for d in data:
        if d == '':
            continue

        if d == 'your ticket:':
            key = 'ticket'
            continue
        elif d == 'nearby tickets:':
            key = 'n_tickets'
            continue

        if key == 'rules':
            rule = d.split(' ')
            rule.pop(-2)
            rule = [i.split('-', ) for i in rule[-2:]]
            rule = [[int(x), int(y)] for x, y in rule]
            notes[key].append(rule)
        else:
            d = [int(i) for i in d.split(',')]
            if key == 'ticket':
                notes[key] += d
            else:
                notes[key].append(d)

    out = 0

    for t in notes['n_tickets']:
        for field in t:
            check = 1
            for r in notes['rules']:
                if r[0][0] <= field <= r[0][1] or r[1][0] <= field <= r[1][1]:
                    check *= 0

            out += (field * check)

    return out


def part_2(data):
    notes = {'rules': [], 'ticket': [], 'n_tickets': []}
    key = 'rules'
    for d in data:
        if d == '':
            continue

        if d == 'your ticket:':
            key = 'ticket'
            continue
        elif d == 'nearby tickets:':
            key = 'n_tickets'
            continue

        if key == 'rules':
            rule = d.split(' ')
            rule.pop(-2)
            rule = [i.split('-', ) for i in rule[-2:]]
            rule = [[int(x), int(y)] for x, y in rule]
            notes[key].append(rule)
        else:
            d = [int(i) for i in d.split(',')]
            if key == 'ticket':
                notes[key] += d
            else:
                notes[key].append(d)

    invalid_tickets = set()

    for idx, t in enumerate(notes['n_tickets']):
        for field in t:
            valid = False
            for r in notes['rules']:
                if r[0][0] <= field <= r[0][1] or r[1][0] <= field <= r[1][1]:
                    valid = True
            if not valid:
                invalid_tickets.add(idx)

    for t in [_ for _ in sorted(invalid_tickets)[::-1]]:
        notes['n_tickets'].pop(t)

    OK = [[True for _ in range(20)] for _ in range(20)]

    for t in notes['n_tickets']:
        for f_idx, field in enumerate(t):
            for r_idx, r in enumerate(notes['rules']):
                if not (r[0][0] <= field <= r[0][1] or r[1][0] <= field <= r[1][1]):
                    OK[f_idx][r_idx] = False

    MAP = [None for _ in range(20)]
    USED = [False for _ in range(20)]
    found = 0

    while True:
        for i in range(20):
            valid_j = [j for j in range(20) if OK[i][j] and not USED[j]]
            if len(valid_j) == 1:
                MAP[i] = valid_j[0]
                USED[valid_j[0]] = True
                found += 1
        if found == 20:
            break

    out = 1
    for idx, i in enumerate(MAP):
        if i < 6:
            out *= notes['ticket'][idx]

    return out

    #
    # import numpy as np
    # from collections import OrderedDict
    #
    # field_pos = np.array(notes['n_tickets']).T
    # matched_fields = OrderedDict()
    #
    #
    # for p_idx, pos in enumerate(field_pos):
    #     tracker = dict()
    #     for field in pos:
    #         for idx, r in enumerate(notes['rules']):
    #             if idx in matched_fields:
    #                 continue
    #             if idx not in tracker:
    #                 tracker[idx] = 0
    #             if r[0][0] <= field <= r[0][1] or r[1][0] <= field <= r[1][1]:
    #                 tracker[idx] += 1
    #
    #     max_n = [0, 0]
    #     for k, v in tracker.items():
    #         if v > max_n[1]:
    #             max_n = k, v
    #
    #     matched_fields[max_n[0]] = p_idx
    #
    # out = 1
    # for a in range(6):
    #     print(data[a], notes['ticket'][matched_fields[a]])
    #     out *= notes['ticket'][matched_fields[a]]
    #
    #
    # return out


if __name__ == '__main__':
    with open('input/16.txt') as f:
        _lines = [_ for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))