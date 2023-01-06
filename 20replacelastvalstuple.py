''' Write a Python program to replace last value of tuples in a list. 
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]'''
aList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
bList = list(aList[0])
cList = list(aList[1])
dList = list(aList[2])
bList.pop()
cList.pop()
dList.pop()
bList.append(100)
cList.append(100)
dList.append(100)
bTuple = tuple(bList) 
cTuple = tuple(cList)
dTuple = tuple(dList)
aList = []
aList.append(bTuple)
aList.append(cTuple)
aList.append(dTuple)
print(aList)
