# a^nb^n word

def is_an_bn(word):
    word = list(word) 
    print (word)
    for i in range (0,len(word)):
        if (word[i] != 'a') and (word[i] != 'b'):
            print(word[i],word)
            print ("false1")
            return False

    if word.count("a") != word.count("b"):
        print("false2")
        return False

    if len(word) % 2 != 0:
        print ("false3")
        return False

    for i in range(0,int(len(word)/2)):
        if word[i] == 'a' and word[-(i+1)]:
            continue
        else:
            print ("False4")
            return False
            break

    print ("True")
    return True

is_an_bn("")
is_an_bn("rado")
is_an_bn("aaabb")
is_an_bn("aaabbb")
is_an_bn("aabbaabb")
is_an_bn("bbbaaa")
is_an_bn("aaaaabbbbb")
