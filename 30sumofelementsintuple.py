'''Write a Python program to compute element-wise sum of given tuples. 
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)'''
aTuple = (1, 2, 3, 4)
bTuple = (3, 5, 2, 1)
cTuple = (2, 2, 3, 1)
oList = []
for i in range(0, len(aTuple)):
    oList.append(aTuple[i]+bTuple[i]+cTuple[i])
print(oList)
