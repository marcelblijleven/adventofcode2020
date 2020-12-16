from unittest import TestCase

from day09.solution import decypher_xmas, find_group_sum, TEST_INPUT


class TestPartOne(TestCase):
    def test_decypher_xmas(self):
        num = decypher_xmas(5, TEST_INPUT)
        self.assertEqual(127, num)


class TestPartTwo(TestCase):
    def test_find_group_sum(self):
        num = decypher_xmas(5, TEST_INPUT)
        group = find_group_sum(TEST_INPUT, num)
        self.assertEqual(62, min(group) + max(group))
