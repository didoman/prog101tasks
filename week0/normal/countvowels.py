#count vowels

def count_vowels(string):
    vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
    counter = 0
    for i in range (0,len(string)):
        if string[i] in vowels:
            counter +=1
    print(counter)
    return counter

count_vowels("Python")
count_vowels("Theistareykjarbunga") #It's a volcano name!
count_vowels("grrrrgh!")
count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
count_vowels("A nice day to code!")