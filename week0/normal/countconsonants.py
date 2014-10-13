#count consonants

def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxz"
    consonants = consonants + consonants.upper()
    counter = 0
    list_of_consonants = []
    #print(consonants)

    list_of_consonants = list(consonants)
    #print(list_of_consonants)
    # sorry, it was easier to populate a list of consonants this way instead of writing it by hand
    for i in range(0,len(string)):
        if string[i] in list_of_consonants:
            counter+=1

    print (counter)
    return counter


count_consonants("asd")
count_consonants("Python")
count_consonants("Theistareykjarbunga") #It's a volcano name!
count_consonants("grrrrgh!")
count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
count_consonants("A nice day to code!")
