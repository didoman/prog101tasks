#iterations of nan expand


def iterations_of_nan_expand(expanded):
    if len(expanded) == 0:
        print(0)
        return 0
    elif "Not a NaN" in expanded:
        counter = expanded.count("Not a")
        print (counter)
        return counter
    else:
        print("False")
        return False

iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN')
iterations_of_nan_expand("")
iterations_of_nan_expand("Not a NaN")
iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN')
iterations_of_nan_expand("Show these people!")
