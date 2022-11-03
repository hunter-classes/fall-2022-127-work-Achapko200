
def fizzbuzz(n):
    number = 1
    while number < n:
        print(number)
        number = number + 1
    for number in range (1,n):
        if number % 3 == 0:
            print ("fizz")
        elif number % 5 == 0:
            print ("buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print ("fizzbuzz")
        else:
            print (number)
    
      
value = 20
print("fizzbuzz up to " , value)
fizzbuzz(value)
