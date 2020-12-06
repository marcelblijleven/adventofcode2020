from util import get_input

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


def part_one(_input):
    total = 0

    for group in groups(_input):
        total += len(group)

    return total


print(part_one(INPUT))
