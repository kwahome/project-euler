def sum_of_multiples(n=0,d=0)
	multiples = (n-(n%d))/d
	return (multiples*(multiples+1)/2) * d
end

t = gets.strip.to_i

for i in 0..t-1
	n = gets.strip.to_i
 	puts sum_of_multiples(n-1, 3) + sum_of_multiples(n-1, 5) - sum_of_multiples(n-1, 3*5)
end