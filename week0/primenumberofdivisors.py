from isprime import is_prime # not sure why, but this will execute the prints in the isprime module
    

def prime_number_of_divisors(n):
    list_of_divisors = [n] 
    
    for i in range(1,n):
        if n % i == 0:
            list_of_divisors.append(i)
    
    #print(list_of_divisors)
    #print(len(list_of_divisors))
    if is_prime(len(list_of_divisors)):
        return True
    else:
        return False


print(prime_number_of_divisors(7))
print(prime_number_of_divisors(8))
print(prime_number_of_divisors(9))
print(prime_number_of_divisors(90))
print(prime_number_of_divisors(19))
