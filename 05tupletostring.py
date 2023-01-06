# Write a Python program to convert a tuple to a string. 
aTuple = ('D', 'a', 'n', 'i', 'e', 'l')
aString = ""
for i in range(0, len(aTuple)):
    aString += aTuple[i]    
print(aString)
