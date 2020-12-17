from util import get_input, solution_timer

TEST_INPUT = list(map(int, get_input('test_input.txt')))
INPUT = list(map(int, get_input('input.txt')))


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


@solution_timer(9, 1)
def part_one(_input, preamble):
    return decypher_xmas(preamble, _input)


def find_group_sum(numbers, target):
    for left_edge in range(len(numbers)):
        for right_edge in range(len(numbers)):
            window = numbers[left_edge:right_edge]
            if sum(window) == target:
                return window


@solution_timer(9, 2)
def part_two(_input, preamble):
    wrong_number = decypher_xmas(preamble, _input)
    group = find_group_sum(_input, wrong_number)
    return min(group) + max(group)


part_one(INPUT, 25)
part_two(INPUT, 25)
