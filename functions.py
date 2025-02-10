import classes
def loopUserInput():
    while input == 'y' or 'Y':
        itemName = input("What is the name of your item :")
        itemRank = input("What do you rank your item: ")

#def searchItem(lst, itemName):

item1 = classes.RankedItem("Fruit1", 4)
item2 = classes.RankedItem("Fruit2", 3)

itemArray = []
itemArray.append(item1)
itemArray.append(item2)
def printItems(lst):
    for i in lst:
        classes.RankedItem(lst[i].define)

printItems(itemArray)