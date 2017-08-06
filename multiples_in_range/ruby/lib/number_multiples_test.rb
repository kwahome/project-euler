require_relative 'number_multiples'
require 'test/unit'

# Testing number multiples
class NumberMultiplesTest < Test::Unit::TestCase
  def setup
    @sum = NumberMultiples.new(10)
  end

  def test_count
    assert_equal(TypeError, @sum.count_multiples_of('a'))
    assert_equal(3, @sum.count_multiples_of(3))
    assert_equal(3, @sum.count_multiples_of('3'))
  end

  def test_list
    expected = {
      1 => 3,
      2 => 6,
      3 => 9
    }
    assert_equal(TypeError, @sum.list_multiples_of('a'))
    assert_equal(expected, @sum.list_multiples_of(3))
    assert_equal(expected, @sum.list_multiples_of('3'))
  end

  def test__sum
    assert_equal(TypeError, @sum.sum_multiples_of(''))
    assert_equal(18, @sum.sum_multiples_of(3))
    assert_equal(18, @sum.sum_multiples_of('3'))
    assert_equal(TypeError, @sum.sum_multiples_of('a', 5))
    assert_equal(23, @sum.sum_multiples_of(3, 5))
    assert_equal(23, @sum.sum_multiples_of('3', 5))
  end

end