#Write a Python program to find the index of an item of a tuple. 
aTuple = (1,2,3,4,5,6,7,8)
yourInput = int(input("Which search item: "))
for i in range(0, len(aTuple)):
    if yourInput == aTuple[i]:
        print("Index: ", i)
