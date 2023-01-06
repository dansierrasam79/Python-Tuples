#Write a Python program to add an item in a tuple. 
aTuple = (1,2,3,4,5)
aList = list(aTuple)
aList.append(6)
aTuple = tuple(aList)
print(aTuple)
