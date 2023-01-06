''' Write a Python program to convert a given list of tuples to a list of lists. 
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]'''
oTuple = [(1, 2), (2, 3), (3, 4)]
sTuple = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
oList = []
for item in oTuple:
    oList.append(list(item))
print(oList)
sList = []
for item in sTuple:
    sList.append(list(item))
print(sList)
