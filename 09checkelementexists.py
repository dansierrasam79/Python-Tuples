#Write a Python program to check whether an element exists within a tuple. 
aTuple = (1,2,3,4,5,6,7,8,6,6)
yourInput = int(input("Enter search item: "))
for item in aTuple:
    if yourInput == item:
        print(yourInput, "is present in search tuple")
