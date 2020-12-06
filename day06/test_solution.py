from unittest import TestCase
from util import get_input
from day06.solution import (
    part_one, part_two,
    groups, groups_as_lists, get_all_answered
)


class TestDay06(TestCase):
    def test_groups(self):
        test_input = get_input('test_input.txt')
        retrieved_groups = list(groups(test_input))

        self.assertTrue(len(retrieved_groups), 5)
        self.assertEqual(retrieved_groups[0], list('abc'))
        self.assertEqual(retrieved_groups[1], list('abc'))
        self.assertEqual(retrieved_groups[2], list('abc'))
        self.assertEqual(retrieved_groups[3], list('a'))
        self.assertEqual(retrieved_groups[4], list('b'))

    def test_groups_as_lists(self):
        test_input = get_input('test_input.txt')
        retrieved_groups = list(groups_as_lists(test_input))
        self.assertTrue(len(retrieved_groups), 5)
        self.assertEqual(retrieved_groups[0], ['abc'])
        self.assertEqual(retrieved_groups[1], ['a', 'b', 'c'])
        self.assertEqual(retrieved_groups[2], ['ab', 'ac'])
        self.assertEqual(retrieved_groups[3], ['a', 'a', 'a', 'a'])
        self.assertEqual(retrieved_groups[4], ['b'])

    def test_get_all_answered(self):
        value = ['abc', 'ab', 'a']
        result = get_all_answered(value)
        self.assertTrue(len(result) == 1)
        self.assertEqual(list(result), ['a'])

        value = ['abc', 'bc', 'bc']
        result = get_all_answered(value)
        self.assertTrue(len(result) == 2)
        self.assertTrue('b' in result)
        self.assertTrue('c' in result)

    def test_part_one(self):
        test_input = get_input('test_input.txt')
        self.assertEqual(part_one(test_input), 11)

    def test_part_two(self):
        test_input = get_input('test_input.txt')
        self.assertEqual(part_two(test_input), 6)
