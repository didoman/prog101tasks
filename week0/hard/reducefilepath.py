# reduce file path

def reduce_file_path(path):
	
	while "//" in path:
		path = path.replace('//', '/')
	
	path = path.split(sep = "/")
	
	print (path)
	while ".." in path:
		prev = path.index("..")
		path.pop(prev-1)
		print (path)
		path.remove("..")
	
	while "." in path:
		path.remove(".")
	
	print (path)
	
reduce_file_path("/home/.././asdf/././/..//new/./paknew/")