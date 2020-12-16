from util import get_input

TEST_INPUT = [int(line) for line in get_input('test_input.txt')]
INPUT = [int(line) for line in get_input('input.txt')]


def decypher_xmas(preamble, numbers):
    idx = preamble

    while preamble < len(numbers):
        preamble_check = numbers[idx - preamble:idx]
        need = numbers[idx]
        seen = []
        is_valid = False
        for num in preamble_check:
            seen.append(num)
            if need - num in seen:
                is_valid = True
                break

        if not is_valid:
            return numbers[idx]

        idx += 1


def part_one(_input, preamble):
    return decypher_xmas(preamble, _input)


def part_two(_input):
    pass


print(part_one(INPUT, 25))
