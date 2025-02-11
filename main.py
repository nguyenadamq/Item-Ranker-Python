#import class
import classes
import functions
#Intro to program
print("Welcome to the Comparative Item Ranker Program!")
itemArray = []

#Start getting user input
itemArray = functions.loopUserInput(itemArray)

#print items in array
print(f"Here is the array of items that you entered: ")
functions.printItems(itemArray)

input = input("\nPress enter to exit.")
