from unittest import TestCase
from day10.solution import find_differences, TEST_INPUT


class TestFindDifferences(TestCase):
    def test_find_differences(self):
        lst = [1, 2, 3, 6, 8, 9]
        differences = find_differences(lst)
        self.assertEqual([1, 1, 1, 2, 3, 2, 1, 3], differences)

    def test_find_differences_with_test_input(self):
        differences = find_differences(TEST_INPUT)
        ones = differences.count(1)
        threes = differences.count(3)
        self.assertEqual(7, ones)
        self.assertEqual(5, threes)
