require_relative 'multiples_in_range'
require 'test/unit'

# Testing sum of multiples
class TestMultiplesInRange < Test::Unit::TestCase
  def setup
    @sum = MultiplesInRange.new(10)
  end

  def test_count
    assert_equal(3, @sum.count_multiples_of(3))
  end

  def test_list
    expected = {
      1 => 3,
      2 => 6,
      3 => 9
    }
    assert_equal(expected, @sum.list_multiples_of(3))
  end

  def test_sum
    assert_equal(18, @sum.sum_multiples_of(3))
  end

end