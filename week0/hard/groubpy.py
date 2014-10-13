# groupby task

def groupby(func, seq):
	output = {}
	for i in range(0,len(seq)):
		funcresult = func(i) # this is made so costly functions are calculated only once per iteration, instead of on every line of code
		if funcresult not in output:
			output[funcresult] = []
		output[funcresult].append(i)
	print (output)
	return output
			
groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7])
groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7])
