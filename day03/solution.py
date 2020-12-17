import unittest
from util import get_input, solution_timer

INPUT = get_input('input.txt')


def evaluate_slope(_input, x_movement, y_movement):
    position = [0, 0]
    grid_width = len(_input[0])
    tree_counter = 0

    while position[1] <= len(_input):
        position[0] += x_movement
        position[1] += y_movement

        if position[0] >= grid_width:
            position[0] = position[0] - grid_width

        x, y = position

        if y >= len(_input):
            break

        if _input[y][x] != ".":
            tree_counter += 1

    return tree_counter


@solution_timer(3, 1)
def part_one(_input):
    return evaluate_slope(_input, 3, 1)


@solution_timer(3, 2)
def part_two(_input):
    import math
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    evaluated = []

    for slope in slopes:
        x, y = slope
        evaluated.append(evaluate_slope(_input, x, y))

    return math.prod(evaluated)


class Day3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_input = ['..##.........##.........##.........##.........##.........##.......',
                          '#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..',
                          '.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.',
                          '..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#',
                          '.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.',
                          '..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....',
                          '.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#',
                          '.#........#.#........#.#........#.#........#.#........#.#........#',
                          '#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...',
                          '#...##....##...##....##...##....##...##....##...##....##...##....#',
                          '.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#']

    def test_part_one(self):
        self.assertEqual(part_one(self.test_input), 7)

    def test_part_two(self):
        self.assertEqual(part_two(self.test_input, 336))


part_one(INPUT)
part_two(INPUT)
