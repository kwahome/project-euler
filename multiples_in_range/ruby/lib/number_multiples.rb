# Class to perform a generic sum of multiples
class NumberMultiples
  def initialize(range)
    raise TypeError unless range.is_a?(Numeric)
    @range = range
  end

  def valid_number?(value)
    value.to_i.zero? && value.to_i.to_s != value ? false : true
  end

  def count_multiples_of(number)
    return TypeError unless valid_number?(number)
    (@range - 1) / number.to_i
  end

  def list_multiples_of(number)
    return TypeError unless valid_number?(number)
    number = number.to_i
    multiples = {}
    count = (@range - 1) / number

    1.upto(count) do |i|
      multiples[i] = i * number
    end
    multiples
  end

  def sum_multiples_of(*numbers)
    sum = 0
    product = 1
    numbers.each do |v|
      return TypeError unless valid_number?(v)
      v = v.to_i
      sum += (((@range - 1) / v) * (((@range - 1) / v) + 1) / 2) * v
      product *= v
    end
    shared_multiples = numbers.length > 1 ? ((@range - 1) / product) : 0
    sum - (shared_multiples * (shared_multiples + 1) / 2) * product
  end
end