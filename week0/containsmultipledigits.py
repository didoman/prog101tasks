# contains multiple digits 

def contains_digits(number, digits):

    number_digits = []
    while number != 0:
        number_digits.append(number%10)
        number = number // 10
    print(number_digits)
    if len([val for val in number_digits if val in digits]) == len(digits):
        print ("True")
    else:
        print("False")

contains_digits(1023, [4,2,3])
contains_digits(402123, [0, 3, 4])
contains_digits(666, [6,4])
contains_digits(123456789, [1,2,3,0])
contains_digits(456, [])
