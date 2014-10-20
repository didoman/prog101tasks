# cat 2
import sys


def cat2(*args):
    # for arg in sys.argv:
    #     print(arg)
    for arg in sys.argv:
        try:
            #print(arg)
            if arg =="cat2.py":
                pass
            print (str(arg) == "cat2.py")
            f = open(arg, 'r')
            content = f.read()
            print(content)
            f.close()
        except FileNotFoundError:
            continue

if __name__ == '__main__':
    cat2()