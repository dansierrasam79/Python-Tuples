'''Write a Python program to remove an empty tuple(s) from a list of tuples. 
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']'''
aList = [(), (), ('a',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
bList = []
for item in aList:
    if type(item) is tuple and len(item) > 0:
        bList.append(item)
print(bList)
