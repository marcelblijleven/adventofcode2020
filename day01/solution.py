from util import get_input

INPUT = get_input('input.txt')


def part_one():
    numbers = map(int, INPUT)
    seen = []

    for number in numbers:
        need = 2020 - number
        if need in seen:
            return need * number
        seen.append(number)


def part_two():
    numbers = map(int, INPUT)

    for a in numbers:
        for b in numbers:
            if (2020 - a - b) in numbers:
                return (2020 - a - b) * a * b


def part_two_v2():
    import math
    from itertools import combinations
    numbers = map(int, INPUT)

    for c in combinations(numbers, 3):
        if sum(c) == 2020:
            print(c)
            return math.prod(c)
