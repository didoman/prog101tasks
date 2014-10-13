# contains digit task 

def contains_digit(number, digit):
    while number != 0:
        if number % 10 == digit:
            print("true")
            return True
        number = number // 10
    print("False")
    return False

contains_digit(10, 1)
contains_digit(123, 1)
contains_digit(42, 2)
contains_digit(10, 3)
contains_digit(123467890, 5)