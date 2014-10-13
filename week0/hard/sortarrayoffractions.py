# sort array of fractions
import operator


def sort_fractions(arr):
    decimal_dict = {}
    for i in range(0, len(arr)):
        nom = arr[i][0]
        denom = arr[i][1]
        decimal = nom/denom
        decimal_dict[(nom,denom)] = decimal

    # i've used stackoverflow for the following line, but it works 
    decimal_sorted = sorted(decimal_dict.items(), key = operator.itemgetter(1))

    sorted_fractions = []
    
    for i in range(0,len(decimal_sorted)):
        sorted_fractions.append(decimal_sorted[i][0])

    print(sorted_fractions)

sort_fractions([(2, 3), (1, 2)])
sort_fractions([(2, 3), (1, 2), (1, 3)])
sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
