import classes
import os
import json
import functions.helper as h
import functions.functions as f

#loop user input
def loopUserInput(itemArray):
    filenum = 1
    option = input("\nChoose an option below(lowercase accepted): " 
                 + "\n(A)  Add items "
                 + "\n(P)  Print items "
                 + "\n(PR) Print items with their rankings"
                 + "\n(U)  Update items"
                 + "\n(R)  Remove items"
                 + "\n(W)  Write to file"
                 + "\n(L)  Load from file"
                 + "\n(E)  Exit program\n"
                 + ": ")

    option = option.lower()
    while option != "e":
        if not option:
            print("Invalid input. Please choose an option.")
        
        elif option == "a":
            #Start getting user input
            itemArray = f.addItem(itemArray)
            
        #Fix this to only print item names
        elif option == "p":
            n = 0
            print(f"\nHere is the list of items: ")
            f.printItems(itemArray, n)
        elif option == "pr":
            n = 1
            print(f"\nHere is the list of items with rankings: ")
            f.printItems(itemArray, n)
        elif option == "u":
            itemArray = f.updateItems(itemArray)
        elif option == "r":
            itemArray = f.removeItems(itemArray)
        elif option == "w":
            filenum = f.writeToFile(itemArray, filenum)
        elif option == "l":
            itemArray = f.loadFromFile(itemArray)
        else:
            print("Invalid choice. Please try again.")

        option = input("\nChoose an option below(lowercase accepted): " 
                 + "\n(A)  Add items "
                 + "\n(P)  Print items "
                 + "\n(PR) Print items with their rankings"
                 + "\n(U)  Update items"
                 + "\n(R)  Remove items"
                 + "\n(W)  Write to file"
                 + "\n(L)  Load from file"
                 + "\n(E)  Exit program\n"
                 + ": ")
        option = option.lower()
    return itemArray
