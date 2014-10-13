# sum numbers in a NxM matrix


def sum_matrix(m):
    thesum = 0
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            thesum = thesum + m[i][j]

    print("sum of matrix numbers",thesum)
    return thesum

if __name__ == '__main__':
    sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
