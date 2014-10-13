#UNFINISHED! discussion in the forums
# spam and eggs task
from math import sqrt

def prepare_meal(number):
	output = ""
	largest_divisor = 1
	
	for i in range (1, number): # if no integer up to the square root of Number is a valid divisor, the Number is prime.
		if number % i == 0:
			#print(number / i, 3**i)
			largest_divisor = int(number/i)
		if 3**i == largest_divisor:
			
			output = i*("spam ")
			break
	
	if i % 3 == 0 and len(output) !=0 :
		output = output + "and eggs"
	elif len(output) == 0:
		output = output + "eggs"
			
	print(output)
	
	
prepare_meal(3)
prepare_meal(9)
prepare_meal(27)
prepare_meal(81)
prepare_meal(5)
prepare_meal(15)
prepare_meal(45)
prepare_meal(360)
prepare_meal(30)