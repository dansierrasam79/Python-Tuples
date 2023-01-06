#Write a Python program to convert a list of tuples into a dictionary. 
aList = [("Zero", "One", "Two"), (0,1,2)]
j = 0
aDict = {}
for i in range(0,len(aList[0])):
    aDict[aList[0][i]] = aList[1][j]
    j += 1
print(aDict)
