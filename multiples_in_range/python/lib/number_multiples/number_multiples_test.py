import unittest
from lib.number_multiples.number_multiples import NumberMultiples


class NumberMultiplesTest(unittest.TestCase):
    """Test class NumberMultiples"""
    def setUp(self):
        """
        This method is called before each test
        """
        self.multiples = NumberMultiples(n=10)

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_count(self):
        self.assertRaises(TypeError, lambda: self.multiples.count_multiples_of('a'))
        self.assertEqual(self.multiples.count_multiples_of(3), 3)
        self.assertEqual(self.multiples.count_multiples_of('3'), 3)

    def test_list(self):
        expected = {
            1: 3,
            2: 6,
            3: 9
        }
        self.assertRaises(TypeError, lambda: self.multiples.list_multiples_of('a'))
        self.assertEqual(self.multiples.list_multiples_of(3), expected)
        self.assertEqual(self.multiples.list_multiples_of('3'), expected)

    def test_sum(self):
        self.assertRaises(TypeError, lambda: self.multiples.sum_multiples_of('a'))
        self.assertEqual(self.multiples.sum_multiples_of(3), 18)
        self.assertEqual(self.multiples.sum_multiples_of('3'), 18)
        self.assertRaises(TypeError, lambda: self.multiples.sum_multiples_of('a', 5))
        self.assertEqual(self.multiples.sum_multiples_of('3', 5), 23)
        self.assertEqual(self.multiples.sum_multiples_of('3', '5'), 23)
