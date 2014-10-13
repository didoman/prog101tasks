# check for inreasing sequence
# not sure if the increase should be made with equal step 
# if so, please refer to the implementation of is_equally_increasing(seq) below 

def is_increasing(seq):
    #increasing sequence would be sorted sequence with no duplicates, so..
    if len(seq) == 1:
        print ("True")
        return True
    elif seq == sorted(seq) and len(seq) == len(set(seq)):
        print ("True")
        return True
    else:
        print ("False")
        return False

def is_equally_increasing(seq):
    if len(seq) == 1:
        print ("True")
        return True
    elif seq == sorted(seq) and len(seq) == len(set(seq)):
        diff = seq[0] - seq[1]
        for i in range(0,len(seq)-1):
            if seq[i] - seq[i+1] != diff:
                print ("False")
                return False
        print ("True")
        return True
    else:
        print("False")
        return False



is_increasing([1,2,3,4,5])
is_increasing([1,2,3,5,7])
is_increasing([1])
is_increasing([5,6,-10])
is_increasing([1,1,1,1])
print ("now the equal increase step fn")

is_equally_increasing([1,2,3,4,5])
is_equally_increasing([1,2,3,5,7])
is_equally_increasing([1])
is_equally_increasing([5,6,-10])
is_equally_increasing([1,1,1,1])