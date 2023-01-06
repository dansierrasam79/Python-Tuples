'''Write a Python program to convert a given string list to a tuple. 
Original string: python 3.0
<class 'str'>
Convert the said string to a tuple:
('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
<class 'tuple'>'''

myString = "python 3.0"
aList = []
aTuple = ()
for character in myString:
    aList.append(character)
aTuple = tuple(aList)
print(aTuple)
