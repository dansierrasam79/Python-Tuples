'''Write a Python program to check if a specified element presents in a tuple of tuples. 
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White present in said tuple of tuples!
True
Check if Olive present in said tuple of tuples!
False'''
def findColor(entry):
    oTuple = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
    for item in oTuple:
        for i in range(0, len(item)):
            if entry == item[i]:
                return True
    return False
if __name__ == "__main__":
    print(findColor("White"))
    print(findColor("Olive"))
