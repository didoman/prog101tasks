#zero insert


def zero_insert(n):
    poslist = []
    n = list(str(n))
    
    for i in range(0,len(n)):
        n[i] = int(n[i])
    #print (n)
    for i in range(0,len(n)-1):
        if (n[i] == n[i+1]) or (n[i]+n[i+1]) % 10 == 0:
            poslist.append(i)
    #print (n,poslist)
    if len(poslist) != 0:
        for i in range(0,len(poslist)):
            pos = poslist.pop()
            #print ("pos:",pos)

            n.insert(pos+1,'0')
            #print(n)
    n = int("".join(str(item) for item in n))
    print(n)
    return n
    



zero_insert(116457)
zero_insert(55555555)
zero_insert(1)
zero_insert(6446)
