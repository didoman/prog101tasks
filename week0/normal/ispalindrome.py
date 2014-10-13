# is palindrome task

def is_int_palindrome(n):
    dupl = n
    reversed_n = 0
    #print(reversed_n)
    
    while dupl != 0:
        reversed_n = reversed_n*10 + (dupl % 10)
        
        dupl = dupl // 10

    #print (n, dupl, reversed_n)

    while reversed_n !=0 and n != 0:
        #print (reversed_n)
        #print (n)
        if reversed_n % 10 == n % 10:
            reversed_n = reversed_n // 10
            n = n // 10
            pass
        else:
            print ("false!!!!!!!!!!!!!!!!!!\n")
            return False
            break
    print("true!!!!!!!!!!!!!!!!!!!!!\n")
    return True

is_int_palindrome(1234)
is_int_palindrome(1234321)
is_int_palindrome(12321)
is_int_palindrome(1000000000001)
is_int_palindrome(1000001000001)
is_int_palindrome(1000010100001)
is_int_palindrome(999)
is_int_palindrome(9919)
is_int_palindrome(99911199)