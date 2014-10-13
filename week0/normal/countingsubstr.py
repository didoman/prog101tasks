#counting substrings task
#the code might look a bit messy, i'm hurrying a lot to finish as much tasks as possible


def count_substrings(haystack, needle):
    outcome = False
    occurance_counter = 0
    haystack_index = 0
    while haystack_index < len(haystack):
        if haystack[haystack_index] == needle[0] and len(haystack[haystack_index:]) >= len(needle):
            #the above line checks if 1st character of "needle" is found somewhere in haystack and
            #remaining haystack string lenght is enough to contain the whole needle
            for j in range(0,len(needle)): 
                #this cycle checks continualy for all consequent needle characters
                if haystack[haystack_index+j] == needle[j]: 
                    outcome = True
                else: 
                    outcome = False
                    haystack_index+=1
                    break
            if outcome == True:
                #we skip cycles in haystack string with the lenght of the needle 
                haystack_index += len(needle)
                occurance_counter +=1
        else: 
            haystack_index+=1
    #print (outcome)

    print ("occuraces = ",occurance_counter)
    return occurance_counter

count_substrings("isaiskaisasiisais", "isa")
count_substrings("siasskaiassiias", "is")
count_substrings("This is a test string", "is")
count_substrings("babababa", "baba")
count_substrings("Python is an awesome language to program in!", "o")
count_substrings("We have nothing in common!", "really?")
count_substrings("This is this and that is this", "this")  # "This" != "this"

