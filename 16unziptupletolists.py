#Write a Python program to unzip a list of tuples into individual lists. 
aTuple = ([1,2,3], [4,5,6])
aList = []
bList = []
aList, bList = aTuple[0], aTuple[1]
print(aList, bList)
