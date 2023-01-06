#Write a Python program to find the repeated items of a tuple. 
aTuple = (1,2,3,4,5,6,7,8,6,6)
aDict = {}
for item1 in aTuple:
    count = 0
    for item2 in aTuple:
        if item1 == item2:
            count += 1
        if count >= 2:
            aDict[item1] = count
print(aDict)
