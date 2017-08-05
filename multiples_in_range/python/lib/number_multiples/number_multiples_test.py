import unittest
from number_multiples import NumberMultiples


class NumberMultiplesTest(unittest.TestCase):
    """Test class NumberMultiples"""
    def setUp(self):
        self.multiples = NumberMultiples(n=10)

    def test_count(self):
        self.assertEqual(self.multiples.count_multiples_of(3), 3)

    def test_list(self):
        expected = {
            1: 3,
            2: 6,
            3: 9
        }
        self.assertEqual(expected, self.multiples.list_multiples_of(3))

    def test_sum(self):
        self.assertEqual(18, self.multiples.sum_multiples_of(3))
