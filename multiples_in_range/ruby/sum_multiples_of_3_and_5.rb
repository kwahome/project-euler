require_relative 'lib/number_multiples'

# def sum_of_multiples(n=0,d=0)
#   multiples = (n-1)/d
#   return (multiples*(multiples+1)/2) * d
# end
#
# t = gets.strip.to_i
#
# 1.upto(t) do
#   n = gets.strip.to_i
#   puts sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 3*5)
# end

n = gets.strip.to_i
sum = NumberMultiples.new(n)

puts sum.sum_multiples_of(3, 5)
