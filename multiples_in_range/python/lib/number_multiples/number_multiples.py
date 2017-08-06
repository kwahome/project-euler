class NumberMultiples:
    """Multiples of numbers in range"""
    def __init__(self, n):
        valid_number, number = self._number(n)
        if valid_number:
            self.n = number
        else:
            raise ValueError(number)

    def _number(self, number):
        try:
            number = int(number)
            result = True, number
        except Exception as e:
            result = False, e
        return result

    def count_multiples_of(self, divisor):
        valid_number, number = self._number(divisor)
        if valid_number:
            response = int((self.n - 1) / number)
        else:
            response = "[ValueError]: {divisor} is not a number".format(divisor=divisor)
        return response

    def list_multiples_of(self, divisor):
        valid_number, number = self._number(divisor)
        if valid_number:
            multiples = {}
            count = int((self.n - 1) / number)
            for index in range(0, count):
                factor = index + 1
                multiples[factor] = factor * number

            response = multiples
        else:
            response = "[ValueError]: {divisor} is not a number".format(divisor=divisor)
        return response

    def sum_multiples_of(self, *args):
        result = 0
        product = 1
        for arg in args:
            valid_number, number = self._number(arg)
            if not valid_number:
                return "[ValueError]: {divisor} is not a number".format(divisor=arg)
            else:
                count = int((self.n - 1) / number)
                result += (count * (count + 1) / 2) * number
                product *= number
        shared_multiples = int(((self.n - 1) / product)) if len(args) > 1 else 0
        result -= (shared_multiples * (shared_multiples + 1) / 2) * product
        return result
