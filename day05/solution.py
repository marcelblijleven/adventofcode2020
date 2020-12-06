import statistics

from util import get_input

INPUT = get_input('input.txt')


def get_midpoint(min_row, max_row):
    return round(statistics.median(range(min_row, max_row + 1)))


def parse(sequence, min_row, max_row):
    next_step = sequence.pop(0)

    if next_step in ['F', 'L']:
        # Take lower half, subtract 1 because you take the lower part until the midpoint
        max_row = get_midpoint(min_row, max_row) - 1
        if not sequence:
            return min_row

    elif next_step in ['B', 'R']:
        # Take upper half
        min_row = get_midpoint(min_row, max_row)
        if not sequence:
            return max_row

    return parse(sequence, min_row, max_row)


def part_one(_input):
    ids = []

    for boarding_pass in _input:
        row = parse([char for char in boarding_pass if char in ['F', 'B']], 0, 127)
        column = parse([char for char in boarding_pass if char in ['L', 'R']], 0, 7)
        ids.append(row * 8 + column)

    return max(ids)


def part_one_binary_option(_input):
    ids = []

    for boarding_pass in _input:
        # could also use a translation table
        # boarding_pass.translate(str.maketrans({'B': '1', 'F': '0', 'R': '1', 'L': '0'})
        boarding_pass = boarding_pass\
            .replace('B', '1')\
            .replace('F', '0')\
            .replace('R', '1')\
            .replace('L', '0')
        ids.append(int(boarding_pass, 2))

    return max(ids), ids


def part_two(_input):
    max_id, ids = part_one_binary_option(_input)

    for _id in range(0, max_id):
        if _id not in ids and _id - 1 in ids and _id + 1 in ids:
            return _id


print(part_one(INPUT))
print(part_one_binary_option(INPUT))
print(part_two(INPUT))
