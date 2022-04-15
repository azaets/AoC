import re
from collections import Counter, OrderedDict
import itertools
from copy import deepcopy


def rec_combat(p1_deck, p2_deck, root = False):
    history = {'p1': set(), 'p2': set()}
    while p1_deck and p2_deck:
        if str([k for k in p1_deck]) in history['p1'] and str([k for k in p2_deck]) in history['p2']:
            if root:
                return p1_deck, p2_deck
            else:
                return 1

        history['p1'].add(str([k for k in p1_deck]))
        history['p2'].add(str([k for k in p2_deck]))

        p1_card = p1_deck.popitem(last=False)[0]
        p2_card = p2_deck.popitem(last=False)[0]

        if p1_card <= len(p1_deck) and p2_card <= len(p2_deck):
            temp_p1_deck = deepcopy(p1_deck)
            temp_p2_deck = deepcopy(p2_deck)
            while len(temp_p1_deck) > p1_card:
                temp_p1_deck.popitem()
            while len(temp_p2_deck) > p2_card:
                temp_p2_deck.popitem()

            winner = rec_combat(temp_p1_deck, temp_p2_deck)

            if winner == 1:
                for c in [p1_card, p2_card]:
                    p1_deck[c] = ''
            elif winner == 2:
                for c in [p2_card, p1_card]:
                    p2_deck[c] = ''

        elif p1_card > p2_card:
            for c in [p1_card, p2_card]:
                p1_deck[c] = ''
        else:
            for c in [p2_card, p1_card]:
                p2_deck[c] = ''

    if root:
        return p1_deck, p2_deck
    else:
        return 1 if len(p1_deck) > len(p2_deck) else 2


def part_2(data):

    p1_deck = OrderedDict()
    p2_deck = OrderedDict()

    cur_player = 0

    for d in data:
        if 'Player 1' in d:
            cur_player = 1
        elif 'Player 2' in d:
            cur_player = 2
        else:
            if cur_player == 1:
                p1_deck[int(d)] = ''
            elif cur_player == 2:
                p2_deck[int(d)] = ''

    p1_deck, p2_deck = rec_combat(p1_deck, p2_deck, root=True)

    out = 0
    for idx, k in enumerate(p1_deck) if len(p1_deck) > len(p2_deck) else enumerate(p2_deck):
        out += k * (max(len(p1_deck), len(p2_deck)) - idx)

    return out


def part_1(data):

    p1_deck = OrderedDict()
    p2_deck = OrderedDict()

    cur_player = 0

    for d in data:
        if 'Player 1' in d:
            cur_player = 1
        elif 'Player 2' in d:
            cur_player = 2
        else:
            if cur_player == 1:
                p1_deck[int(d)] = ''
            elif cur_player == 2:
                p2_deck[int(d)] = ''

    while p1_deck and p2_deck:
        p1_card = p1_deck.popitem(last=False)[0]
        p2_card = p2_deck.popitem(last=False)[0]
        if p1_card > p2_card:
            for c in [p1_card, p2_card]:
                p1_deck[c] = ''
        else:
            for c in [p2_card, p1_card]:
                p2_deck[c] = ''

    out = 0
    for idx, k in enumerate(p1_deck) if len(p1_deck) > len(p2_deck) else enumerate(p2_deck):
        out += k * (max(len(p1_deck), len(p2_deck)) - idx)

    return out


if __name__ == '__main__':
    with open('input/22.txt') as f:
        _lines = [_ for _ in f.read().splitlines() if _ != '']

    print(part_1(_lines))
    print(part_2(_lines))