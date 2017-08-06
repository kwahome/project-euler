require_relative 'lib/number_multiples'
n = gets.strip.to_i
sum = NumberMultiples.new(n)

puts sum.sum_multiples_of(3, 5)
