# nan expand

def nan_expand(times):
    if times == 0:
        print("")
    elif times < 0:
        print("bad input")
    else:
        expanded = times*"Not a "
        print(not_a + "NaN")
        return expanded

if __name__ == '__main__':
    nan_expand(0)
    nan_expand(-1)
    nan_expand(1)
    nan_expand(2)
    nan_expand(5)
    nan_expand(10)
