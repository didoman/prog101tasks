# list to number

def list_to_number(digits):
    # we convert each item in "digits" list to string, join these tiny strings 
    # together in a previously empty string and finally, convert it to int
    print(int("".join(str(item) for item in digits)))
    return int("".join(str(item) for item in digits)) 

list_to_number([1,2,3])
list_to_number([9,9,9,9,9])
list_to_number([1,2,3,0,2,3])
