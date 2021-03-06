from util import get_input, solution_timer

INPUT = get_input('input.txt')
TEST_INPUT = get_input('test_input.txt')


def groups(_input: list[str]) -> list[str]:
    group = ''
    for line in _input:
        if line:
            group += line
        else:
            yield sorted(list(set(list(group))))
            group = ''

    yield sorted(list(set(list(group))))


def groups_as_lists(_input: list[str]) -> list[list[str]]:
    group = []
    for line in _input:
        if line:
            group.append(line)
        else:
            yield group
            group = []

    yield group


def get_all_answered(value: list[str]) -> list[str]:
    s = set(value[0])

    for i in range(1, len(value)):
        s = s & set(value[i])

    return s


@solution_timer(6, 1)
def part_one(_input):
    total = 0

    for group in groups(_input):
        total += len(group)

    return total


@solution_timer(6, 2)
def part_two(_input):
    total = 0

    for group in groups_as_lists(_input):
        total += len(get_all_answered(group))

    return total


part_one(INPUT)
part_two(INPUT)
