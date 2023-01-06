''' Write a Python program to calculate the product, multiplying all the numbers of a given tuple. 
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648'''
aTuple = (4, 3, 2, 2, -1, 18)
bTuple = (2, 4, 8, 8, 3, 2, 9)
aProduct = 1
bProduct = 1
for item in aTuple:
    aProduct *= item
for item in bTuple:
    bProduct *= item
print(aProduct, bProduct)
