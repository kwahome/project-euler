require_relative 'lib/multiples_in_range'
n = gets.strip.to_i
sum = MultiplesInRange.new(n)

puts sum.sum_multiples_of(3) +
     sum.sum_multiples_of(5) -
     sum.sum_multiples_of(3 * 5)