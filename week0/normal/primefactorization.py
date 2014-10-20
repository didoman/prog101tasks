#prime factorization


def prime_factorization(number):

    factor = 2
    factor_power = 0
    answerset = []
    factorlist = []

    while factor <= number and number > 1:
        if number % factor == 0:
            number = int(number/factor)
            factorlist.append(factor)
        else:
            if factor in factorlist:
                answerset.append((factor, factorlist.count(factor)))
            factor+=1
    if factor in factorlist:
        answerset.append((factor,factorlist.count(factor)))
    print (answerset)
    return answerset

prime_factorization(10)
prime_factorization(14)
prime_factorization(356)
prime_factorization(89)
prime_factorization(1000)
