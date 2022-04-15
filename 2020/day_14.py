import re
from collections import Counter
import itertools
from copy import deepcopy

def part_2(data):
    print(data)
    mask = ''
    combinations = []
    out = dict()

    for i in data:
        if i[:3] == 'mas':
            mask = i.split(' = ')[1]
            floating_bit_count = Counter(mask)['X']
            combinations = list(itertools.product([0, 1], repeat=floating_bit_count))
        else:
            addr = [_ for _ in format(int(re.findall(r'\[(.*?)\]', i)[0]), '036b')]
            i = int(i.split(' = ')[1])
            for comb in combinations:
                tmp_addr = deepcopy(addr)
                comb_idx = 0
                for idx, bit in enumerate(mask):
                    if bit == 'X':
                        tmp_addr[idx] = str(comb[comb_idx])
                        comb_idx += 1
                    elif bit == '1':
                        tmp_addr[idx] = bit

                out[int(''.join(tmp_addr), 2)] = i

    return sum(out.values())


def part_1(data):
    print(data)
    mask = ''
    out = dict()

    for i in data:
        if i[:3] == 'mas':
            mask = i.split(' = ')[1]
        else:
            addr = re.findall(r'(?<=\[).+?(?=\])', i)[0]
            i = [_ for _ in format(int(i.split(' = ')[1]), '036b')]
            for idx, bit in enumerate(mask):
                if bit != 'X':
                    i[idx] = bit
            out[addr] = int(''.join(i), 2)

    return sum(out.values())


if __name__ == '__main__':
    with open('input/14.txt') as f:
        _lines = [_ for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))