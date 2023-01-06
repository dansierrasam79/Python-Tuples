# Write a Python program to convert a tuple to a dictionary. 
aTuple = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight")
aDict = {}
for i in range(0, len(aTuple)):
    aDict[aTuple[i]] = i
print(aDict)
