from unittest import TestCase

from day09.solution import decypher_xmas, TEST_INPUT


class Test(TestCase):
    def test_decypher_xmas(self):
        num = decypher_xmas(5, TEST_INPUT)
        self.assertEqual(127, num)
