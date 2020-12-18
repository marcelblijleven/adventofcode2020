from util import get_input, solution_timer
from operator import itemgetter


TEST_INPUT = get_input('test_input.txt')
INPUT = get_input('input.txt')
FREE_SEAT = 'L'
FLOOR = '.'
TAKEN_SEAT = '#'


def get_layout(lines):
    y = 0
    layout = {}

    for line in lines:
        x = 0
        for item in line:
            layout[x, y] = item
            x += 1
        y += 1

    return layout


def get_x_y_range(layout):
    max_x = max(layout.keys(), key=itemgetter(0))[0]
    max_y = max(layout.keys(), key=itemgetter(1))[1]
    return max_x, max_y


def get_adjacent_coordinates(layout, current_x, current_y):
    adjacent_coordinates = {}

    for x, y in [(current_x + i, current_y + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]:
        if (x, y) in layout:
            adjacent_coordinates[x, y] = layout[x, y]

    return adjacent_coordinates


def seating_iteration(layout):
    new_layout = layout.copy()
    max_x, max_y = get_x_y_range(layout)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if layout[x, y] == FLOOR:
                continue

            adjacent_coordinates = get_adjacent_coordinates(layout, x, y)

            if layout[x, y] == FREE_SEAT:
                if [v for k, v in adjacent_coordinates.items() if k != (x, y)].count(TAKEN_SEAT) == 0:
                    new_layout[x, y] = TAKEN_SEAT
            elif layout[x, y] == TAKEN_SEAT:
                if [v for k, v in adjacent_coordinates.items() if k != (x, y)].count(TAKEN_SEAT) >= 4:
                    new_layout[x, y] = FREE_SEAT

    return new_layout


def print_layout(layout):
    max_x, max_y = get_x_y_range(layout)
    lines = []

    for y in range(max_y + 1):
        line = ''
        for x in range(max_x + 1):
            line += layout[x, y]

        lines.append(line)

    print('\n'.join(lines), '\n')


def start_iterating(layout):
    previous_layout = layout
    iteration = 1

    while True:
        new_layout = seating_iteration(previous_layout)
        if new_layout == previous_layout:
            return len([value for value in new_layout.values() if value == TAKEN_SEAT])

        previous_layout = new_layout
        iteration += 1


@solution_timer(day=11, part=1)
def part_one(_input):
    layout = get_layout(_input)
    taken_seats = start_iterating(layout)
    return taken_seats


def part_two(_input):
    pass


part_one(TEST_INPUT)
