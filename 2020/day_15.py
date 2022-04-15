
def part_2(data):
    pos_tracker = dict()

    for idx, d in enumerate(data, 1):
        pos_tracker[d] = idx

    turn_counter = len(data)
    prev_numb = data[-1]
    pos_tracker.pop(prev_numb)
    current_numb = 0

    while turn_counter < 30000000:
        if prev_numb in pos_tracker:
            current_numb = turn_counter - pos_tracker[prev_numb]
            pos_tracker[prev_numb] = turn_counter
            prev_numb = current_numb
        else:
            pos_tracker[prev_numb] = turn_counter
            prev_numb = 0

        turn_counter += 1

    return current_numb

def part_1(data):
    pos_tracker = dict()

    for idx, d in enumerate(data, 1):
        pos_tracker[d] = idx

    turn_counter = len(data)
    prev_numb = data[-1]
    pos_tracker.pop(prev_numb)
    current_numb = 0

    while turn_counter < 2020:
        if prev_numb in pos_tracker:
            current_numb = turn_counter - pos_tracker[prev_numb]
            pos_tracker[prev_numb] = turn_counter
            prev_numb = current_numb
        else:
            pos_tracker[prev_numb] = turn_counter
            prev_numb = 0

        turn_counter += 1

    return current_numb


if __name__ == '__main__':
    _lines = [int(i) for i in '5,2,8,16,18,0,1'.split(',')]

    print(part_1(_lines))
    print(part_2(_lines))