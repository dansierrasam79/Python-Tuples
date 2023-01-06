# Write a Python program to count the elements in a list until an element is a tuple. 
aList = ['a', 1, 'b', 2, 'c', 3, 'd', 4, (16,2), 'e', 5]
count = 0
for item in aList:
    if type(item) is not tuple:
        count += 1
    else:
        break;
print(count)
