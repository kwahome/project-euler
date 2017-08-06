import unittest
from lib.number_multiples.number_multiples import NumberMultiples


class NumberMultiplesTest(unittest.TestCase):
    """Test class NumberMultiples"""
    def setUp(self):
        self.multiples = NumberMultiples(n=10)

    def test_count(self):
        self.assertEqual(self.multiples.count_multiples_of('a'), '[ValueError]: a is not a number')
        self.assertEqual(self.multiples.count_multiples_of(3), 3)
        self.assertEqual(self.multiples.count_multiples_of('3'), 3)

    def test_list(self):
        expected = {
            1: 3,
            2: 6,
            3: 9
        }
        self.assertEqual(self.multiples.list_multiples_of('a'), '[ValueError]: a is not a number')
        self.assertEqual(self.multiples.list_multiples_of(3), expected)
        self.assertEqual(self.multiples.list_multiples_of('3'), expected)

    def test_sum(self):
        self.assertEqual(self.multiples.sum_multiples_of('a'), '[ValueError]: a is not a number')
        self.assertEqual(self.multiples.sum_multiples_of(3), 18)
        self.assertEqual(self.multiples.sum_multiples_of('3'), 18)
        self.assertEqual(self.multiples.sum_multiples_of('a', 5), '[ValueError]: a is not a number')
        self.assertEqual(self.multiples.sum_multiples_of('3', 5), 23)
        self.assertEqual(self.multiples.sum_multiples_of('3', '5'), 23)
