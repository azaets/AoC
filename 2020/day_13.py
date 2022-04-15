def part_2_brute(data):

    pattern = dict()
    gap = 0

    for c, d in enumerate(data[1].split(',')):
        if d == 'x':
            gap += 1
        else:
            pattern[int(d)] = gap
            gap += 1

    brute_buses = [i for i in pattern]
    brute_numb = int(data[1].split(',')[0])

    accum = 25141499100000-(25141499100000 % brute_numb)

    gap_len = len(data[1].split(','))

    x = 0

    while x != 1:
        x = 1
        for i in pattern:
            x += (accum+pattern[i]) % i

        print(accum, x)

        if x == 1:
            return accum

        accum += brute_numb

        # if accum > 1068789:
        #     return accum

    return accum

    # buses = [int(i) for i in data[1].split(',') if i != 'x']
    # pass

def mod_pow(b, e, mod):
    if e == 0:
        return 1
    elif e%2 == 0:
        return mod_pow((b*b)%mod, e/2, mod)
    else:
        return (b*mod_pow(b, e-1, mod))%mod

def mod_inverse(a, m):
    return mod_pow(a, m-2, m)

def part_2(data):
    bus_sched = data[1].split(',')

    constr = []
    N = 1

    for i, b in enumerate(bus_sched):
        if b != 'x':
            b = int(b)
            i %= b
            constr.append(((b-i) % b, b))
            N *= b

    ans = 0
    for i, bus_id in constr:
        NI = N//bus_id
        MI = mod_inverse(NI, bus_id)
        for_b = i*MI*NI
        ans += for_b

    ans %= N

    return ans



def part_1(data):
    timestamp = int(data[0])
    buses = [int(i) for i in data[1].split(',') if i != 'x']

    l_min = [timestamp, 0]

    for b in buses:
        if (b - (timestamp % b)) < l_min[0]:
            l_min[0] = b - (timestamp % b)
            l_min[1] = b

    return l_min[0] * l_min[1]


if __name__ == '__main__':
    with open('input/13.txt') as f:
        _lines = [_ for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))