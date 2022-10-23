def find_smallest(thelist):
    small_so_far = thelist[0]
    for item in thelist[1:]:
        if item < small_so_far:
            small_so_far = item
    return small_so_far
  
  
  
  
  def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))
