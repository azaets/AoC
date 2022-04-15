import re, math
from collections import OrderedDict
import itertools

def part_2(data):
    pass

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def check_rule(rules, subrules, initial = False):
    if not subrules:
        return []

    sub_r = []
    matches = []
    for rule in subrules:
        sub_r = rules[rule].split(' | ')
        if len(sub_r[0]) < 2:
            matches.append(sub_r)
        else:
            _sub_r = [map(int, _.split(' ')) for _ in sub_r]
            for r in _sub_r:
                __matches = check_rule(rules, [int(_) for _ in r])
                _matches = []
                if len(r) == 2 and len(__matches) <= 2:
                    for i in __matches:
                        if type(i) == list and len(i) == 1:
                            _matches += i[0]
                        else:
                            _matches += i
                    print(__matches, r)
                    _matches = ''.join([_ for _ in _matches])
                    matches.append(_matches)
                else:
                    matches.append(__matches)

            if len(sub_r) > 1 and len(matches) > 3:
                permut = set()
                a,b = split_list(matches)
                for i in a:
                    for j in b:
                        try:
                            permut.add(i + j)
                        except:
                            permut.add(i[0][0] + j[0][0])
                matches = list(permut)



    return matches[0] if initial else matches



def part_1(data):
    _rules = [l for l in data if len(re.findall(r'\b[\d\:].*\b', l)) > 0]
    _msgs = [l for l in data if len(re.findall(r'\b[\d\:].*\b', l)) == 0]

    rules = OrderedDict()

    for r in sorted(_rules):
        rule, subrule = r.split(': ')
        rules[int(rule)] = subrule

    matches = check_rule(rules, [0], True)

    print(matches)

    # permut = dict()
    # for i in range(len(matches)):
    #     for k in matches[i]:
    #         for j in range(i + 1, len(matches)):
    #             for m in matches[j]:
    #                 permut[k + m] = 0
    #
    out = 0
    #
    # print(permut)

    x = []
    for i in matches:
        for j in i:
            x.append(j)

    y = list(itertools.combinations(x, 3))

    permut = dict()
    for v in y:
        add = ''
        for k in v:
            add += k
        permut[add] = ''

    for m in _msgs:
        if m in permut:
            out += 1

    return out

if __name__ == '__main__':
    with open('input/19.txt') as f:
        _lines = [_.replace('"', '') for _ in f.read().splitlines() if _ != '']

    print(part_1(_lines))
    print(part_2(_lines))