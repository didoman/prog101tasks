# biggest difference between two numbers

def biggest_difference(arr):
    # we sort the list of integers and return the result of the first minus last element
    arr = sorted(arr)
    print (arr[0] - arr[-1])
    return arr[0] - arr[-1]



biggest_difference([1,2])
biggest_difference([1,2,3,4,5])
biggest_difference([-10, -9, -1])
biggest_difference(range(100))
