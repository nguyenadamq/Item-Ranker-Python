#import class
import classes
import functions
#Intro to programitem
print("Welcome to the Comparative Item Ranker Program!")
itemArray = []

#Start getting user input
itemArray = functions.loopUserInput(itemArray)

#print items in array
functions.printItems(itemArray)

option = input("\nWould you like to continue adding?(Y/y) or (N/n): ")
option = option.lower()
while option != "n":
    if not option:
        print("Invalid input. Please choose an option.")
        option = input("\nWould you like to continue adding?(Y/y) or (N/n): ")
    elif option == "y":
        #Start getting user input
        itemArray = functions.loopUserInput(itemArray)
        #print items in array
        functions.printItems(itemArray)
        option = input("\nWould you like to continue adding?(Y/y) or (N/n): ")
        option = option.lower()

input = input("\nPress enter to exit.")
