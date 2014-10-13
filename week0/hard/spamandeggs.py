#UNFINISHED! discussion in the forums
# spam and eggs task
from math import sqrt

def prepare_meal(number):
    output = ""
    largest_divisor = 1

    for i in range (1, number): 
        if number % 3**i == 0:
            output = i*"spam "


    if number % 5 == 0 and len(output) !=0 :
        output = output + "and eggs"
    elif len(output) == 0:
        output = output + "eggs"

    print(output)
	
	
prepare_meal(3)
prepare_meal(9)
prepare_meal(27)
# prepare_meal(81)
prepare_meal(5) # eggs
prepare_meal(15) # spam and eggs , because 15 / 3 and 3**1 = 3 => 1x spam
prepare_meal(45) # spam spam and eggs , because 45 / 9 and 3**2 = 9 => 2x spam
# prepare_meal(360)
# prepare_meal(30)