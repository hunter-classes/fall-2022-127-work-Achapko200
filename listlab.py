def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))




def get_odd_numbers(numbers):
    odd_numbers = []

    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)

    return odd_numbers
  
  
  
  
 def upper(word):
    
    first = word[0]
    if first in 'aeiouAEIOU':
        result = word + 'ay'
    else:
        if first == first.upper():
            result = word[1:].capitalize()+first.lower()+'ay'
        else:
            result = word[1:]+first+'ay'
    
    return result
  
  
  
  
