from util import get_input, solution_timer

INPUT = get_input('input.txt')


@solution_timer(1, 1)
def part_one():
    numbers = map(int, INPUT)
    seen = []

    for number in numbers:
        need = 2020 - number
        if need in seen:
            return need * number
        seen.append(number)


@solution_timer(1, 2)
def part_two():
    numbers = map(int, INPUT)

    for a in numbers:
        for b in numbers:
            if (2020 - a - b) in numbers:
                return (2020 - a - b) * a * b


@solution_timer(1, 2)
def part_two_v2():
    import math
    from itertools import combinations
    numbers = map(int, INPUT)

    for c in combinations(numbers, 3):
        if sum(c) == 2020:
            return math.prod(c)


part_one()
part_two()
part_two_v2()
