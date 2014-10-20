#cat command
import sys


def cat(arg):
    try:
        f = open(arg, 'r')
        content = f.read()
        print (content)
        f.close()
    except FileNotFoundError:
        print ("no such file")

if __name__ == '__main__':
    for arg in sys.argv:
        cat(arg)
