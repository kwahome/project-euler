class NumberMultiples:
    """Multiples of numbers in range"""
    def __init__(self, n):
        self.n = n

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
