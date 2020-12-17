from collections import defaultdict

from util import get_input, solution_timer

TEST_INPUT = list(map(int, get_input('test_input.txt')))
INPUT = list(map(int, get_input('input.txt')))


def find_differences(_input):
    working_list = sorted([0] + _input + [max(_input) + 3])
    differences = [y - x for x, y in zip(working_list[:-1], working_list[1:])]
    return differences


@solution_timer(day=10, part=1)
def part_one(_input):
    differences = find_differences(_input)
    ones = differences.count(1)
    threes = differences.count(3)
    return ones * threes


@solution_timer(day=10, part=2)
def part_two(_input):
    jolts = sorted([0] + _input + [max(_input) + 3])
    cache = defaultdict(int, {0: 1})

    for a, b in zip(jolts[1:], jolts):
        cache[a] = cache[a - 3] + cache[a - 2] + cache[a - 1]

    return cache[jolts[-1]]


part_one(INPUT)
part_two(INPUT)
