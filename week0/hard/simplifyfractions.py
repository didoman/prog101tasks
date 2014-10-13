# simplify fractions 

def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    reduced_fraction = fraction

    smaller_of_two = 0
    if nominator <= denominator:
        smaller_of_two = nominator
    else:
        smaller_of_two = denominator

    for i in list(range(smaller_of_two,1,-1)):
        # print(i,nominator,denominator,smaller_of_two)
        if (nominator % i == 0) and (denominator % i == 0):
            # print (nominator % i, denominator % i)

            reduced_fraction = (int(nominator/i),int(denominator/i))
            # print (nominator/i, denominator/i, reduced_fraction)
            #break
    print (reduced_fraction)

simplify_fraction((3,9))
simplify_fraction((9,6))
simplify_fraction((16,9))
simplify_fraction((6,66))
simplify_fraction((12,15))
simplify_fraction((15,21))   
simplify_fraction((11,22))
