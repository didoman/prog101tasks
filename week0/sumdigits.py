# sum all digits of a number

def sum_all_digits(n):
	sumall = 0
	while n != 0:
		sumall = sumall + n % 10 
		n = n//10
	return sumall

print(sum_all_digits(1))
print(sum_all_digits(123))
print(sum_all_digits(101))
print(sum_all_digits(100))
print(sum_all_digits(123))
print(sum_all_digits(14543252))
print(sum_all_digits(1123321))
