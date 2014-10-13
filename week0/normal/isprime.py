# check if an integer is prime number

def is_prime(n):
    if n < 0:
        n = -n

    if n == 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        # print(int(n ** 0.5)+1)
        # print(i)
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(8))
print(is_prime(11))
print(is_prime(-10))
print(is_prime(41))
print(is_prime(447))
print(is_prime(443))
