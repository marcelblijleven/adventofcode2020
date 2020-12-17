import re
from util import get_input, solution_timer

INPUT = get_input('input.txt')

TEST_INPUT = get_input('test_input.txt')
TEST_INPUT2 = get_input('test_input2.txt')

bag_type_pattern = re.compile(r'^([a-z]+ [a-z]+)')
contents_pattern = re.compile(r'((\d) ([a-z]+ [a-z]+))')
gold_bag = 'shiny gold'


@solution_timer(7, 1)
def part_one(_input):
    bags = get_bags(_input)
    gold_holders = []
    for bag in bags:
        if search(bags, bag, gold_bag):
            gold_holders.append(bag)

    return len(gold_holders), gold_holders


@solution_timer(7, 2)
def part_two(_input):
    bags = get_bags(_input)
    return bag_counter(gold_bag, bags, 1, 0)


def get_bags(_input):
    bags = {}

    for line in _input:
        bag = bag_type_pattern.match(line).group()
        contents = contents_pattern.findall(line)
        bags[bag] = {}

        for content in contents:
            _, number_str, _bag = content
            bags[bag][_bag] = int(number_str)

    return bags


def search(bags, current_bag, bag):
    contents = [content for content in bags[current_bag].keys()]
    if contents:
        for content in contents:
            if content == bag:
                return True
            else:
                if search(bags, content, bag):
                    return True
    else:
        return False


def bag_counter(bag, bags, multiplier, total):
    contents = bags[bag]
    total += sum([multiplier * value for _, value in contents.items()])

    for k, v in contents.items():
        total = bag_counter(k, bags, v * multiplier, total)

    return total


part_one(INPUT)
part_two(INPUT)
