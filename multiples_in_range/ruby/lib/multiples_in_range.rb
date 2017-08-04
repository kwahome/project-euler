# Class to perform a generic sum of multiples
class MultiplesInRange
  def initialize(range)
    raise unless range.is_a?(Numeric)
    @n = range
  end

  def count_multiples_of(divisor)
    (@n - 1) / divisor
  end

  def list_multiples_of(divisor)
    multiples = {}
    count = (@n - 1) / divisor

    1.upto(count) do |i|
      multiples[i] = i * divisor
    end
    multiples
  end

  def sum_multiples_of(divisor)
    count = (@n - 1) / divisor
    (count * (count + 1) / 2) * divisor
  end
end