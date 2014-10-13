# count unique words in list of words

def unique_words_count(arr):
	i=0
	uniques = 0
	
	while len(arr) != 0:
		word = arr[0]
		i = arr.count(word)
		uniques+=1
		
		# while word in arr:
			# arr.remove(word)
		for i in range (0,i):
			arr.remove(word)
		
	print (uniques)
	return uniques

unique_words_count(["apple", "banana", "apple", "pie"])
unique_words_count(["python", "python", "python", "ruby"])
unique_words_count(["HELLO!"] * 10)
unique_words_count(['pie', 'pie', 'apple', 'juice'])