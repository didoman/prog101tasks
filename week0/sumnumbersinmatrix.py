# sum numbers in a NxM matrix

def sum_matrix(m):
    thesum = 0
    for i in range(0,len(m)):
        subma3x = m[i]
        for j in range(0,len(subma3x)):
            thesum = thesum + subma3x[j]

    print(thesum)
    return thesum

sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
