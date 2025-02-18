#import class
import classes
import functions.functions as functions
import json
import functions.mainloop as m

#Intro to program
print("Welcome to the Comparative Item Ranker Program!")
itemArray = []

#Start getting user input
itemArray = m.loopUserInput(itemArray)

functions.testWriteToJson()
