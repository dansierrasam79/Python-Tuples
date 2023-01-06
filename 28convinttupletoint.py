'''Write a Python program to convert a given tuple of positive integers into an integer. 
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570''' 
oTuple = (1,2,3)
sTuple = (10, 20, 40, 5, 70)
myString = ""
for item in oTuple:
    myString += str(item)
print(myString)
myString2 = ""
for item in sTuple:
    myString2 += str(item)
print(myString2)
