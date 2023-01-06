#Write a Python program to reverse a tuple. 
aTuple = (1,2,3,4,5,6)
aList = list(aTuple)
bList = []
for i in range(len(aList)-1, -1, -1):
    bList.append(aList[i])
print(bList)
