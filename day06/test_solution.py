from unittest import TestCase
from util import get_input
from day06.solution import groups


class Test(TestCase):
    def test_groups(self):
        test_input = get_input('test_input.txt')
        retrieved_groups = list(groups(test_input))

        self.assertTrue(len(retrieved_groups), 5)
        self.assertEqual(retrieved_groups[0], list('abc'))
        self.assertEqual(retrieved_groups[1], list('abc'))
        self.assertEqual(retrieved_groups[2], list('abc'))
        self.assertEqual(retrieved_groups[3], list('a'))
        self.assertEqual(retrieved_groups[4], list('b'))
