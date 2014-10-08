# sum of all divisors of a given integer

def sum_of_divisors(n):
    list_of_divisors = [] # helper, disregard
    divsum = n # every number divides itself
    for i in range(1,n):
        if n % i == 0:
            list_of_divisors.append(i)
            divsum += i

    #print(list_of_divisors)
    return divsum

print(sum_of_divisors(3))
print(sum_of_divisors(5))
print(sum_of_divisors(10))
print(sum_of_divisors(12))
print(sum_of_divisors(20))
print(sum_of_divisors(66))
print(sum_of_divisors(100))
print(sum_of_divisors(8))
print(sum_of_divisors(7))
print(sum_of_divisors(1000))
