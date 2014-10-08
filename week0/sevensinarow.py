# N sevens in a row task

def sevens_in_a_row(arr, n):
    if 7 not in arr:
        return False #if there are no 7s - it's obviosly false
    elif arr.count(7) < n:
        return False #if the number of 7s is less than the row lenght we seek - it's obviously false
    else:
        list_of_indexes = []
        for i in range(0,len(arr)):
            if arr[i] == 7:
                for j in range (i,i+n):
                    #print(i,i+n) #debug
                    if arr[j] != 7:
                        break
                    else:
                        #print(arr[j]) #debug
                        return True
            list_of_indexes.append(i)
        print(list_of_indexes)
        







print(sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
print(sevens_in_a_row([10,8,1,6,1,1,1,20,-7], 3))
print(sevens_in_a_row([1,7,1,7,7], 4))
print(sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
print(sevens_in_a_row([7,2,1,6,2], 1))
print(sevens_in_a_row([7,2,1,6,2], 2))
print(sevens_in_a_row([7,2,1,6,7], 2))
print(sevens_in_a_row([1,2,1,6,7], 1))
print(sevens_in_a_row([1,2,1,6,7,2,7,7], 2))
