# reduce file path

def reduce_file_path(path):
    
    while "//" in path:
        path = path.replace('//', '/')
        #print(path)
        if len(path) == 0:
            path = "/"

    path = path.split(sep = "/")
    #print(path)

    while "." in path:
        path.remove(".")
    
    while "" in path:
        path.remove("")

    #print (path)

    while ".." in path and len(path) > 1:
        prev = path.index("..")
        path.pop(prev-1)
        #print (path)
        path.remove("..")
    if ".." in path and len(path) == 1:
        path.remove("..")
        
    #print (path)
    
    newpath = "/"
    if len(path) >0:
        for i in range(0,len(path)):
            if path[i] != "":
                newpath = newpath + path[i] + "/"
        #print (newpath[-1])
        
        if newpath[-1] == "/" and len(newpath) != 0:
            newpath = newpath[:len(newpath)-1]
        #print(len(newpath))    
    
    print(newpath)

reduce_file_path("/home/.././asdf/././/..//new/./paknew/")  #new/paknew
reduce_file_path("/")                                       #/
reduce_file_path("/srv/../")                                #/
reduce_file_path("/srv/www/htdocs/wtf/")                    #/srv/www/htdocs/wtf
reduce_file_path("/srv/www/htdocs/wtf")                     #/srv/www/htdocs/wtf
reduce_file_path("/srv/./././././")                         #/srv
reduce_file_path("/etc//wtf/")                              #/etc/wtf
reduce_file_path("/etc/../etc/../etc/../")                  #/
reduce_file_path("//////////////")                          #/
reduce_file_path("/../")                                    #/
