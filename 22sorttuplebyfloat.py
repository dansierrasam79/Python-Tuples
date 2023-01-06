''' Write a Python program to sort a tuple by its float element. 
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]'''
aList = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
fList = []
finalList = []
for i in range(0, len(aList)):
    fList.append(aList[i][1])
fsList = sorted(fList)
for i in range(0, len(fsList)):
    for j in range(0, len(fsList)):
        if fsList[i] == aList[j][1]:
            finalList.append(aList[j])
print(finalList)
