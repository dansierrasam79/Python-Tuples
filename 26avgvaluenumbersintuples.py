'''Write a Python program to calculate the average value of the numbers in a given tuple of tuples. 
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
[25.5, -18.0, 3.75]'''
oTuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
oList = []
sList = []
for i in range(0, len(oTuple)):
    total = 0
    for j in range(0, len(oTuple[i])):
        total += oTuple[j][i]
    oList.append(total/len(oTuple[i]))
sTuple = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
for i in range(0, len(sTuple[0])):
    total = 0
    for j in range(0, len(sTuple)):
        total += sTuple[j][i]
    sList.append(total/len(sTuple))
print(sList)
