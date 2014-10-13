# count words from harder problem set


def count_words(arr):
	i = 0
	words = {}
	while len(arr) != 0:
		i = arr.count(arr[0])
		words[arr[0]] = i
		word = arr[0]
		for i in range (0, i):
			arr.remove(word)
		print ('lenght =', len(arr))
	print (words)
	return words
		
		
		
count_words(['pie', 'pie', 'apple', 'juice'])
count_words(["apple", "banana", "apple", "pie"])
count_words(["python", "python", "python", "ruby"])
