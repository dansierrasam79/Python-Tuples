'''Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples. 
Original list of tuples:
[(1, 2), (2, 3), (3, 4)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[3, 5, 7]
Original list of tuples:
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[9, -1, 7, 8]'''
oTuple = [(1, 2), (2, 3), (3, 4)]
sTuple = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
oList = []
sList = []
for item in oTuple:
    total = 0
    for i in range(0, len(item)):
        total += item[i]
    oList.append(total)
for item in sTuple:
    total = 0
    for i in range(0, len(item)):
        total += item[i]
    sList.append(total)
print(oList, sList)
