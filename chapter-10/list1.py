myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList.append(True)
myList.append(4)
myList.append(76)

myList.append(["apple", 76])
myList.insert(3, "cat")
myList.insert(0, 99)
print(myList.index("hello"))
print(myList)
myList.count(76)
myList.remove(76)
myList.pop(myList.index(True))
print(myList)
