# hack numbers
from ispalindrome import is_int_palindrome


def to_bin(number):
    strbin = str(bin(number))
    strbin = strbin[2:len(strbin)]
    return strbin


def next_hack(number):
    answer = False

    while answer is False:
        number += 1
        worked_number = to_bin(number)

        ones = worked_number.count('1')
        # print(worked_number, ones)
        if ones % 2 == 0:
            continue

        if len(worked_number) == 1:
            print(number)
            answer = True
            break
            return 1

        if is_int_palindrome(int(worked_number)):
            answer = True
            worked_number = "0b" + worked_number
            print (int(worked_number,2))
            return int(worked_number,2)

next_hack(0)
next_hack(6)
next_hack(10)
next_hack(20)
next_hack(7910)
next_hack(8031)
