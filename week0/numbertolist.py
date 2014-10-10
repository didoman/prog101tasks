#turn a number into a list of digits

def number_to_list(n):
    n = list(str(n))
    for i in range(0,len(n)):
        n[i] = int(n[i])
    print (n)
    return n
    

number_to_list(123)
number_to_list(99999)
number_to_list(123023)
