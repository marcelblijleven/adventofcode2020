from unittest import TestCase

from day11.solution import (
    get_adjacent_coordinates, get_layout, get_x_y_range,
    start_iterating, TEST_INPUT
)


class Test(TestCase):
    def test_get_layout(self):
        lines = ['123', '456']
        layout = get_layout(lines)

        self.assertEqual('1', layout[0, 0])
        self.assertEqual('2', layout[1, 0])
        self.assertEqual('3', layout[2, 0])
        self.assertEqual('4', layout[0, 1])
        self.assertEqual('5', layout[1, 1])
        self.assertEqual('6', layout[2, 1])

    def test_get_x_y_range(self):
        layout = {
            (0, 1): 'test',
            (1, 1): 'test',
            (2, 2): 'test',
            (3, 2): 'test',
        }

        max_x, max_y = get_x_y_range(layout)
        self.assertEqual(3, max_x)
        self.assertEqual(2, max_y)

    def test_get_adjacent_coordinates(self):
        lines = [
            '123',
            '456',
            '789',
        ]

        layout = get_layout(lines)

        x, y = 0, 0
        coords = get_adjacent_coordinates(layout, x, y)

        self.assertTrue((0, 1) in coords.keys())
        self.assertTrue((1, 0) in coords.keys())
        self.assertTrue((1, 1) in coords.keys())

        x, y = 1, 1
        coords = get_adjacent_coordinates(layout, x, y)

        self.assertTrue((0, 0) in coords.keys())
        self.assertTrue((0, 1) in coords.keys())
        self.assertTrue((0, 2) in coords.keys())
        self.assertTrue((1, 0) in coords.keys())
        self.assertTrue((1, 2) in coords.keys())
        self.assertTrue((2, 0) in coords.keys())
        self.assertTrue((2, 1) in coords.keys())
        self.assertTrue((2, 2) in coords.keys())

    def test_start_iterating(self):
        layout = get_layout(TEST_INPUT)
        result = start_iterating(layout)
        self.assertEqual(37, result)
