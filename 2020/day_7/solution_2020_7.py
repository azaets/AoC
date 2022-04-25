from abc import ABC
from collections import defaultdict
from copy import deepcopy
import numpy as np

from aoc_tools.challenge import Challenge
from aoc_tools.parser import Parser
from aoc_tools.utils import display_return_value, verify_sample_input


class InputParser(Parser, ABC):
    def __init__(self):
        super(InputParser, self).__init__()

    def get_bag_contents(self):
        for rule in self.puzzle_input():
            bag_contents = defaultdict(dict)
            parent_bag, contents = self.get_parent_bag(rule)
            for child_bag in self.get_children_bags(contents):
                if child_bag is None:
                    continue
                else:
                    bag_contents[parent_bag.strip()].update(child_bag)

            yield bag_contents

    @staticmethod
    def get_parent_bag(rule: str):
        return rule.split("bags contain", maxsplit=1)

    @staticmethod
    def get_children_bags(contents: str):
        bags = contents.split(', ')

        for bag in bags:
            bag = bag.strip()  # Remove leading/trailing spaces
            bag_quantity, bag_color = bag.split(' ', maxsplit=1)
            if bag_quantity == "no":
                yield None
            else:
                bag_color = ' '.join(bag_color.split(' ')[:2])
                yield {bag_color: bag_quantity}


class Solution(Challenge, ABC):
    def __init__(self, year: int, day: int):
        super().__init__(year, day)
        self.input_parser: InputParser = ...

        self.my_bag = "shiny gold"

    @verify_sample_input(expected_sample_output=4)
    def solution_part_1(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        bags_map = dict()

        for bag_contents in self.input_parser.get_bag_contents():
            bags_map.update(bag_contents)

        big_bag_count = 0
        checked_bags = set()
        discovery_queue = [bag_color for bag_color, contents in bags_map.items() if self.my_bag in contents]

        while discovery_queue:
            next_queue = deepcopy(discovery_queue)
            discovery_queue = list()
            for bag in next_queue:
                if bag in checked_bags:
                    continue
                checked_bags.add(bag)  # Skipp checked bags to ensure cycle prevention

                big_bag_count += 1

                discovery_queue.extend([bag_color for bag_color, contents in bags_map.items() if bag in contents])

        return big_bag_count

    @verify_sample_input(expected_sample_output=32)
    def solution_part_2(self, sample_input=True):
        self.input_parser.set_input(sample_input=sample_input)

        bags_map = dict()

        for bag_contents in self.input_parser.get_bag_contents():
            bags_map.update(bag_contents)

        def count_bags(next_parent_bag_color, next_parent_bag_count):

            if (next_parent_bag_color not in bags_map) or (bags_map[next_parent_bag_color] is None):
                return int(next_parent_bag_count)

            parent_bag_count = 0

            for bag_color, count in bags_map[next_parent_bag_color].items():
                parent_bag_count += count_bags(bag_color, count)

            return int(next_parent_bag_count) * parent_bag_count + int(next_parent_bag_count)

        return count_bags(self.my_bag, 1) - 1


if __name__ == '__main__':
    puzzle = Solution(2020, 7)
    puzzle.reload_challenge_inputs()
    
    parser = InputParser()
    puzzle.register_input_parser(parser)
    
    puzzle.solution_part_1()
    puzzle.solution_part_2()
