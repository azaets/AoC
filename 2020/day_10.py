def find_permutations(data, adapter = 0, mem = {}):
    if adapter == len(data) - 1:
        return 1

    if adapter in mem:
        return mem[adapter]

    permutation_counter = 0

    for next_adapter in range(adapter+1, len(data)):
        if data[next_adapter] - data[adapter] <= 3:
            permutation_counter += find_permutations(data, next_adapter, mem)
    mem[adapter] = permutation_counter

    return permutation_counter

def part_1(data):
    d = {1:0, 2:0, 3:0}

    for i in range(1, len(data)):
        d[data[i]-data[i-1]] += 1

    return d[1] * d[3]

def part_2(data):
    return find_permutations(data)


if __name__ == '__main__':
    with open('input/10.txt') as f:
        _lines = [int(_) for _ in f.read().splitlines()]

    _lines += [0]
    _lines.sort()
    _lines += [_lines[-1]+3]

    print(part_1(_lines))
    print(part_2(_lines))