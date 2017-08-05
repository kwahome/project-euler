class NumberMultiples:
    """Multiples of numbers in range"""
    def __init__(self, n):
        try:
            int(n)
        except ValueError:
            raise ValueError

        self.n = n

    def count_multiples_of(self, divisor):
        return (self.n - 1) / divisor

    def list_multiples_of(self, divisor):
        multiples = {}
        count = (self.n - 1) / divisor

        for index in range(0, count):
            factor = index + 1
            multiples[factor] = factor * divisor

        return multiples

    def sum_multiples_of(self, divisor):
        count = (self.n - 1) / divisor
        return (count * (count + 1) / 2) * divisor
