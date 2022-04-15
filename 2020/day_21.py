import re
from collections import Counter
import itertools
from copy import deepcopy


def part_2(data):
    original_input = dict()
    ingredient_map = dict()
    all_ingredients = set()

    for idx, d in enumerate(data):
        allergens = re.findall(r'\(([^\)]+)\)', d)[0][9:].split(', ')
        ingredients = d.replace(' (' + re.findall(r'\(([^\)]+)\)', d)[0] + ')', '').split(' ')

        original_input[idx] = (set(ingredients))

        for i in ingredients:
            all_ingredients.add(i)

        for a in allergens:
            if a not in ingredient_map:
                ingredient_map[a] = set(ingredients)
            else:
                ingredient_map[a] = ingredient_map[a].intersection(set(ingredients))

    for i in ingredient_map:
        all_ingredients.difference_update(ingredient_map[i])

    done = False

    while not done:
        done = True

        for i in ingredient_map:
            if len(ingredient_map[i]) == 1:
                for j in ingredient_map:
                    if i != j:
                        ingredient_map[j].difference_update(ingredient_map[i])
            else:
                done = False

    out = dict()
    for i in ingredient_map:
        if ingredient_map[i]:
            out[i] = ingredient_map[i].pop()

    return ','.join([out[i] for i in sorted(out)])


def part_1(data):

    original_input = dict()
    ingredient_map = dict()
    all_ingredients = set()

    for idx, d in enumerate(data):
        allergens = re.findall(r'\(([^\)]+)\)', d)[0][9:].split(', ')
        ingredients = d.replace(' (' + re.findall(r'\(([^\)]+)\)', d)[0] + ')', '').split(' ')

        original_input[idx] = (set(ingredients))

        for i in ingredients:
            all_ingredients.add(i)

        for a in allergens:
            if a not in ingredient_map:
                ingredient_map[a] = set(ingredients)
            else:
                ingredient_map[a] = ingredient_map[a].intersection(set(ingredients))

    for i in ingredient_map:
        all_ingredients.difference_update(ingredient_map[i])

    out = 0
    for i in all_ingredients:
        for ii in original_input:
            if i in original_input[ii]:
                out += 1

    return out

if __name__ == '__main__':
    with open('input/21.txt') as f:
        _lines = [_ for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))