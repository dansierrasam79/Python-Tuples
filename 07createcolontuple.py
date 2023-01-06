#Write a Python program to create the colon of a tuple. 
import copy
tuplex = ("HELLO", 5, [], True) 
print(tuplex)
#make a copy of a tuple using deepcopy() function
tuplex_colon = copy.deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)
