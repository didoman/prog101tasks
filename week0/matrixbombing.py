#matrix bombing
# in the current implementation, matrixes are handled in this directions:
#        x=0          x = max
#    y=0--------------------->
#       | (0,0)      (max, 0)
#       |
#       |
#       |
# y=max v (0,max)    (max,max)
#
# or simply put: y = 0 is at highest point, not at lowest point
# i found it to be easier for printing
#
# finally, the code may not be in best condition, but
# i'll refine it later, the deepcopy thing took too much
# health and armor already



from sumnumbersinmatrix import sum_matrix
from copy import deepcopy

def matrix_bombing_plan(m):
    choice_set = {}
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            choice_set[(i,j)]=0

    print(choice_set)
    print()
    for i in choice_set.keys():
        after_bombing_matrix = deepcopy(m)
        print ("coordinates hit:", i)
        after_bombing_matrix = alter_matrix_helper(after_bombing_matrix,i)
        matrix_printer_helper(after_bombing_matrix)
        print()
        choice_set[i] = sum_matrix(after_bombing_matrix)
    print()
    print (choice_set)
    for i in choice_set.keys():
        print (i,"=",choice_set[i])
    return choice_set

def alter_matrix_helper(m,tup): 
    k,v = tup[0],tup[1]
    if k-1 >= 0:
        m[k-1][v] -=9
        if v-1 >=0:
            m[k-1][v-1] -=9
        if v+1 < len(m[k]):
            m[k-1][v+1] -=9
    if k+1 <len(m):
        m[k+1][v] -=9
        if v-1 >= 0:
            m[k+1][v-1] -=9
        if v+1 < len(m[k]):
            m[k+1][v+1] -=9
    if v-1 >= 0:
        m[k][v-1] -=9
    if v+1 <len(m[k]):
        m[k][v+1] -=9

    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            if m[i][j] < 1:
                m[i][j] = 1
    return m

def matrix_printer_helper(m):
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            print ("'",m[i][j],"'",end="")
        print ()

matrix_bombing_plan([[10,10,10],[10,10,10],[10,10,10]])
matrix_bombing_plan([[10,10,10,10],[10,10,10,10],[10,10,10,10]])
matrix_bombing_plan([[10,10,10],[10,10,10],[10,10,10],[10,10,10]])
matrix_bombing_plan([[10,10],[10,10],[10,10]])
matrix_bombing_plan([[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10]])
matrix_bombing_plan([[10,10,10],[10,10,10],[10,10,10]])
matrix_bombing_plan([[3,3,3],[3,3,3],[3,3,3]])