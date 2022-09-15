def is_even(n):
    return n % 2 == 0



def is_odd(n):
    if is_even(n):
        print ("This is an even integer.")
    else:
        print ("This is an odd integer.")
    return n % 2 != 0



def is_even(n):
    return n % 2 == 0



def is_odd(n):
    if is_even(n):
        print ("This is an even integer.")
    else:
        print ("This is an odd integer.")
    return n % 2 != 0


a = input("Enter a ")
b = input("Enter b ")
c = input("Enter c ")


def isright_angled():
    if abs((a**2+b**2)-(c**2)) < 0.1 or abs((c**2-a**2)-(b**2)) < 0.1 or abs((c**2-b**2)-(a**2)) < 0.1:                         
        return True
    else:
        return False

print (isright_angled)()

