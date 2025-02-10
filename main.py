#import class
import classes

#Intro to program
print("Welcome to the Comparative Item Ranker Program!")

itemName = input("What is the name of your item :")
itemRank = input("What do you rank your item: ")

item = classes.RankedItem(itemName, itemRank)

itemArray = []
itemArray.append(item)



