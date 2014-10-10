#is decreasing 
#basically, it's a copy paste of is increasing task, but reverse sorting requires a new list revseq

def is_decreasing(seq):
    revseq = seq[:]
    revseq.sort()
    revseq.reverse()
    if len(seq) == 1:
        print ("True")
        return True
    elif seq == revseq and len(seq) == len(set(seq)):
        print ("True")
        return True
    else:
        print ("False")
        return False

def is_equally_decreasing(seq):
    revseq = seq[:]
    revseq.sort()
    revseq.reverse()
    if len(seq) == 1:
        print ("True")
        return True
    elif seq == revseq and len(seq) == len(set(seq)):
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

is_decreasing([4,3,2,1])
is_decreasing([4,3,2,1,-1])
is_decreasing([1])
is_decreasing([1,2,3,4])
is_decreasing([4,1,3,2])
print ("now the equal decrease step fn")
is_equally_decreasing([4,3,2,1])
is_equally_decreasing([4,3,2,1,-1])
is_equally_decreasing([1])
is_equally_decreasing([1,2,3,4])
is_equally_decreasing([4,1,3,2])