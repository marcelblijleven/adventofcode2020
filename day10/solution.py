from util import get_input

TEST_INPUT = [int(line) for line in get_input('test_input.txt')]
INPUT = [int(line) for line in get_input('input.txt')]


def find_differences(_input):
    working_list = sorted([0] + _input + [max(_input) + 3])
    differences = [y - x for x, y in zip(working_list[:-1], working_list[1:])]
    return differences


def part_one(_input):
    differences = find_differences(_input)
    ones = differences.count(1)
    threes = differences.count(3)
    return ones * threes


def part_two(_input):
    pass


print(part_one(INPUT))
