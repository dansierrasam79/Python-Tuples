''' Write a Python program to convert a tuple of string values to a tuple of integer values. 
Original tuple values:
(('333', '33'), ('1416', '55'))
New tuple values:
((333, 33), (1416, 55))'''
oTuple = (('333', '33'), ('1416', '55'))
sTuple = ()
oList = []
fList = []
for item in oTuple:
    for i in range(0, len(item)):
        oList.append(int(item[i]))
    fList.append(tuple(oList))
    oList = []
sTuple = tuple(fList)
print(sTuple)
