# is number balanced

def is_number_balanced(number):
    number_digits = []
    leftside = []
    leftsidesum = 0
    rightside = []
    rightsidesum = 0

    while number != 0:
        number_digits.append(number%10)
        number = number // 10
    print(number_digits)

    if len(number_digits) == 1:
        print ("True")
        return True
        #print ("this is balanced")
    elif len(number_digits) % 2 != 0:
        number_digits.pop(int(len(number_digits)/2))

    for i in range (0,int(len(number_digits)/2)):
        leftside.append(number_digits[i]) 
    for i in range (int(len(number_digits)/2),len(number_digits)):
        rightside.append(number_digits[i])

    for i in range(0,len(leftside)):
        leftsidesum = leftsidesum + leftside[i]
    for i in range(0,len(rightside)):
        rightsidesum = rightsidesum + rightside[i]
    if leftsidesum == rightsidesum:
        print ("True")
        return True
    else:
        print ("False")
        return False
    # print(leftside)
    # print(rightside)
    # print(number_digits)
    # print(leftsidesum)
    # print(rightsidesum)

is_number_balanced(4324)
is_number_balanced(9)
is_number_balanced(11)
is_number_balanced(13)
is_number_balanced(121)
is_number_balanced(4518)
is_number_balanced(28471)
is_number_balanced(1238033)
