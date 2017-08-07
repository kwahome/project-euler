from functools import reduce


class NumberMultiples:
    """Multiples of numbers in range"""
    def __init__(self, n=1000000):
        valid_number, number = self._number(n)
        if valid_number:
            self.n = number

    def _number(self, number):
        try:
            num = int(number)
            return True, num
        except Exception:
            raise TypeError('[ValueError]: {num} is not a valid number'.format(num=number))

    def _gcd(self, num1, num2):
        valid_num1, num1 = self._number(num1)
        valid_num2, num2 = self._number(num2)
        if valid_num1 and valid_num2:
            while num2:
                num1, num2 = num2, num1 % num2
            return num1

    def _lcm(self, num1, num2):
        valid_num1, num1 = self._number(num1)
        valid_num2, num2 = self._number(num2)
        if valid_num1 and valid_num2:
            return (num1 * num2) / self._gcd(num1, num2) if self._gcd(num1, num2) is not 0 else 0

    def lcm_of(self, *args):
        return reduce(self._lcm, args)

    def gcd_of(self, *args):
        return reduce(self._gcd, args)

    def count_multiples_of(self, divisor):
        valid_number, number = self._number(divisor)
        if valid_number:
            return int((self.n - 1) / number)

    def least_multiple_of(self, divisor):
        valid_number, number = self._number(divisor)
        if valid_number:
            return number

    def greatest_multiple_of(self, divisor):
        valid_number, number = self._number(divisor)
        if valid_number:
            return int((self.n - 1) / number) * number

    # TODO: Use generator
    # TODO: Optimize to constant time
    def list_multiples_of(self, divisor):
        valid_number, number = self._number(divisor)
        if valid_number:
            multiples = {}
            count = int((self.n - 1) / number)
            for index in range(0, count):
                factor = index + 1
                multiples[factor] = factor * number
            return multiples

    # TODO: Use generator
    # TODO: Optimize to constant time
    def list_common_multiples_of(self, *args):
        multiples = {}
        for arg in args:
            valid_number, number = self._number(arg)
            if valid_number:
                count = int((self.n - 1) / self.lcm_of(*args))
                for index in range(0, count):
                    factor = index + 1
                    multiples[factor] = factor * self.lcm_of(*args)
                return multiples

    def sum_multiples_of(self, *args):
        result = 0
        product = 1
        for arg in args:
            valid_number, number = self._number(arg)
            if valid_number:
                count = int((self.n - 1) / number)
                result += (count * (count + 1) / 2) * number
                product *= number
        shared_multiples = int(((self.n - 1) / product)) if len(args) > 1 else 0
        result -= (shared_multiples * (shared_multiples + 1) / 2) * product
        return result
