#Write a Python program to remove an item from a tuple. 
aTuple = (1,2,3,4,5,6,7,8)
aList = []
yourInput = int(input("Which item do you want to delete? ")) 
aList = list(aTuple)
aList.remove(yourInput)
print(tuple(aList))
