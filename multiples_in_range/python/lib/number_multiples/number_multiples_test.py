import unittest
import number_multiples.NumberMultiples


class NumberMultiplesTest(unittest.TestCase):

    """Test class NumberMultiples"""
    def setUp(self):
        self.n = 10

    def count_multiples_of(self, divisor):
        return (self.n - 1) / divisor

    def list_multiples_of(self, divisor):
        multiples = {}
        count = (self.n - 1) / divisor

        for index in range(1, count):
            multiples[index] = index * divisor

        return multiples

    def sum_multiples_of(self, divisor):
        count = (self.n - 1) / divisor
        return (count * (count + 1) / 2) * divisor
