def is_even(n):
    return n % 2 == 0



def is_odd(n):
    if is_even(n):
        print ("This is an even integer.")
    else:
        print ("This is an odd integer.")
    return n % 2 != 0
