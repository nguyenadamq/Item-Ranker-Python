import classes
import os
import json
import functions.helper as h

#function to run merge sort of itemRanks within itemArray
def sort(itemArray):
    if len(itemArray) <= 1:
        return itemArray
    
    #initialize middle point
    mid = len(itemArray) // 2

    #Recursively check each side
    left_side = sort(itemArray[:mid])

    right_side = sort(itemArray[mid:])


    return h.merge(left_side, right_side)

#CREATE item
def addItem(itemArray):
    n = -1
    #initial inputs
    itemName = input("\nWhat is the name of your item: ")
    while not itemName:
        print("Invalid input. Please enter a name for your item.")
        itemName = input("\nWhat is the name of your item: ")

    if len(itemArray) >= 1:
        #search item for duplicate
        n = searchItem(itemArray, itemName)
    
    ranked = False
    while(n != -1):

        #Duplicate found and print index
        print(f"The name {itemName} is found at index {n} (loopuser)")
        option = input("Would you like to overwrite(O/o) or enter a new item?(N/n)? ")
        option.lower()

        #Input validation
        while (option != "o") and (option != "n"):
            print("Invalid input. Please check the input options and try again.")
            option = input("Would you like to overwrite(O/o) or enter a new item?(N/n)? ")
        
        if option == "o":
            itemArray = overwrite(itemArray,n)
            n = -1
            print("Item has been successfully overwritten.")
            ranked = True

        #user chooses new name
        else:
            itemName = input("\nWhat is the name of your item: ")
            #search item for duplicate
            n = searchItem(itemArray, itemName)
            ranked = False

    #move here is item wasnt ranked during override
    if ranked == False:
        #get and validate item rank
        while True:
            try:
                itemRank = int(input("What do you rank your item(1-10): "))
                if 1 <= itemRank <= 10:
                    break
                else:
                    print("\nInvalid input. Please enter ranking between 1-10.\n")
            except  ValueError:
                print("Invalid input. Please enter valid integer between 1-10.\n")

        #initialize the item with the class
        item = classes.rankedItem(itemName, itemRank)

        #add the item to the list
        itemArray.append(item)

        #sort itemArray right after append
        itemArray = sort(itemArray)
    #run until the if statement uses break statement(user responds no)
    while True:
        test = input("\nWould you like to add another item?(Y/y) or (N/n): ")

        #if the user wants to continue then reask input
        if str(test).lower() == "y":
            #initial inputs
            itemName = input("\nWhat is the name of your item: ")
            while not itemName:
                print("Invalid input. Please enter a name for your item.")
                itemName = input("\nWhat is the name of your item: ")
            n = searchItem(itemArray, itemName)
            ranked = False
            while(n != -1):

                #Duplicate found and print index
                print(f"The name {itemName} is found at index {n} (loopuser)")
                option = input("Would you like to overwrite(O/o) or enter a new item?(N/n)? ")
                option.lower()

                #Input validation
                while (option != "o") and (option != "n"):
                    print("Invalid input. Please check the input options and try again.")
                    option = input("Would you like to overwrite(O/o) or enter a new item?(N/n)? ")
                
                if option == "o":

                    #get and validate item rank (finishing user input for overwrite)
                    while True:
                        try:
                            itemRank = int(input("What do you rank your item(1-10): "))
                            if 1 <= itemRank <= 10:
                                break
                            else:
                                print("\nInvalid input. Please enter ranking between 1-10.\n")
                        except  ValueError:
                            print("Invalid input. Please enter valid integer between 1-10.\n")
                    
                    item = classes.rankedItem(itemName, itemRank)
                    itemArray[n] = item
                    n = -1
                    #sort array after update with override
                    itemArray = sort(itemArray)

                    print("Item has been successfully overwritten.")
                    ranked = True

                #user chooses new name
                else:
                    itemName = input("\nWhat is the name of your item: ")
                    #search item for duplicate
                    n = searchItem(itemArray, itemName)
                    ranked = False

            #move here is item wasnt ranked during override
            if ranked == False:
                #get and validate item rank
                while True:
                    try:
                        itemRank = int(input("What do you rank your item(1-10): "))
                        if 1 <= itemRank <= 10:
                            break
                        else:
                            print("Invalid input. Please enter ranking between 1-10.")
                    except  ValueError:
                        print("Invalid input. Please enter valid integer between 1-10.\n")

                item = classes.rankedItem(itemName, itemRank)
                itemArray.append(item)

                #sort item Array
                itemArray = sort(itemArray)

        #if user doesnt want to continue then break the outer while loop
        elif str(test).lower() == "n":
            break

        #invalid input then reloop
        else:
            print("Invalid input. Please try again.")

    return itemArray

#function to print all items in the array itemArray and their object values - calling the function "define()" - READ
def printItems(itemArray, n):
    if n == 1:
        print("{", end="")
        if (len(itemArray) - 1) >= 1:
            for i in range(len(itemArray) - 1):
                print(itemArray[i].define(), end=", ")
            print(itemArray[len(itemArray)-1].define(), end="")
        else:
            for i in range(len(itemArray)):
                print(itemArray[i].define(), end="")
        
        print("}")
        return None
    else:
        print("{", end="")
        if (len(itemArray) - 1) >= 1:
            for i in range(len(itemArray) - 1):
                print(itemArray[i].name, end=", ")
            print(itemArray[len(itemArray)-1].name, end="")
        else:
            for i in range(len(itemArray)):
                print(itemArray[i].name, end="")
        
        print("}")
        return None
#print the rankings(to test sort)
def printRankings(itemArray):
    for i in range(len(itemArray)):
        print(itemArray[i].rank, end = " ")
    print("\n")
    return None

#function to search for specific itemName within itemArray - UPDATE
def searchItem(itemArray, searchName):

    #iterate through array of items
    for i in range(len(itemArray)):
        if itemArray[i].name.lower() == searchName.lower():
            return i
    return -1

#UPDATE item
def overwrite(itemArray,itemName, n):
    #get and validate item rank (finishing user input for overwrite)
    itemRank = int(input("What do you rank your item(1-10): "))
    while (itemRank < 1) or (itemRank > 10):
        print("Invalid input. Please enter ranking between 1-10.")
        itemRank = int(input("What do you rank your item(1-10): "))
            
        item = classes.rankedItem(itemName, itemRank)
        itemArray[n] = item

        #sort array after update with override
        itemArray = sort(itemArray)
        print("Item has been successfully updated.")
    return itemArray

#DELETE ITEM
def removeItems(itemArray):
    
    #handle no items in list
    if len(itemArray) < 1:
        print("\nNo items in list. Please add an item first.")
        return itemArray
    
    #initial inputs
    itemName = input("\nWhat is the name of your item: ")

    #validate input to be not empty
    while not itemName:
        print("Invalid input. Please enter a name for your item: ")
        itemName = input("\nWhat is the name of your item: ")

    #find index then remove
    n = searchItem(itemArray, itemName)

    #remove item
    while n == -1:
        #item not found
        print("\n'" + itemName + "'" + " was not found in list.")

        #initial inputs
        itemName = input("\nWhat is the name of your item: ")

        #validate input to be not empty
        while not itemName:
            print("Invalid input. Please enter a name for your item: ")
            itemName = input("\nWhat is the name of your item: ")

        #find index then remove
        n = searchItem(itemArray, itemName)

    #remove the item and print the removed item
    removedItem = itemArray.pop(n)

    print("\n'" + removedItem.name + "'" + " has been removed")
    if len(itemArray) == 0:
        print("\nList is now empty...Returning to options.")
        return itemArray

    option = input("\nWould you like to remove another item(Y/y) or (N/n)")
    option = option.lower()
    while option != "n":
        if not option:
            print("Invalid input. Please enter an option.")
        elif option == "y":
            #initial inputs
            itemName = input("\nWhat is the name of your item: ")

            #validate input to be not empty
            while not itemName:
                print("Invalid input. Please enter a name for your item: ")
                itemName = input("\nWhat is the name of your item: ")

            #find index then remove
            n = searchItem(itemArray, itemName)

            #remove and save item
            removedItem = itemArray.pop(n)

            #print name
            print("\n'" + removedItem.name + "'" + " has been removed")

            #if list becomes empty then exit function
            if len(itemArray) == 0:
                print("\nList is now empty...Returning to options.")
                return itemArray
    return itemArray

def updateItems(itemArray):
    #if the list is empty then exit
    if len(itemArray) < 1:
        print("There are no items in the list to update...Returning to options.")
        return itemArray
    
    #print items with rankings so user may view what to update
    printItems(itemArray, 1)
    #ask for user input on item name
    itemName = input("\nWhat is the name of your item you'd like to update: ")
    
    n = searchItem(itemArray, itemName)

    #while the item is not found
    while(n == -1):
        print(f"\n'{itemName}' was not found in the list. Please enter the item name again.")
        printItems(itemArray, 1)
        itemName = input("\nWhat is the name of your item you'd like to update: ")
        n = searchItem(itemArray, itemName)

    #update item
    itemArray = overwrite(itemArray, itemName, n)

    #ask for option input
    option = input("Would you like to update another item?(Y/y) (N/n): ")
    option.lower()

    #run loop while user wants to continue
    while option == "y":
        itemName = input("\nWhat is the name of your item you'd like to update: ")
        n = searchItem(itemArray, itemName)

        while(n == -1):
            print(f"\n'{itemName}' was not found in the list. Please enter the item name again.")
            itemName = input("\nWhat is the name of your item you'd like to update: ")
            n = searchItem(itemArray, itemName)
        
        itemArray = overwrite(itemArray, itemName, n)
                
        option = input("Would you like to update another item?(Y/y) (N/n): ")
        option.lower()

    #return updated array
    return itemArray

def arrayToString(itemArray):
    #start of file
    sentence = "{"
    #only 1 item then no comma at end
    if len(itemArray) == 1:
        sentence += "'" + itemArray[0].name + "'" + ": " + str(itemArray[0].rank)

    #otherwise add the comma for all except end
    else:
        for i in range(len(itemArray) - 1):
            sentence += "'" + itemArray[i].name + "'" + ": " + str(itemArray[i].rank) + ", "

        sentence += "'" + itemArray[len(itemArray)-1].name + "'" + ": " + str(itemArray[len(itemArray)-1].rank)
    sentence += "}"

    return sentence

def writeToFile(itemArray, filenum):
    #if list is empty then 
    if len(itemArray) < 1:
        print("\nItem list is empty. No file had been made.")
        return filenum
    #otherwise use arrayToString function and print to file
    else:
        sentence = arrayToString(itemArray)
        f = open("./itemlists/itemlist" + str(filenum) + ".txt", "w")
        f.write(sentence)

        #print user statement
        print("\nItem list: ")
        printItems(itemArray, 1)
        print("has been successfully written to " + "itemlist" + str(filenum) + ".txt")


    #increment f for new item file for next time
    filenum = filenum + 1
    return filenum

def loadFromFile(itemArray):
    state = False
    print("\nList of files to load from: ")
    print(os.listdir("./itemlists"))

    filename = input("Which list would you like to load from? (Example: 'itemlist1.txt' -> 'itemlist1'): ")
    filename.lower()

    for file in os.listdir("./itemlists"):
        file.lower()
        if(filename + ".txt" == file):
            state = True
    if state == False:
        print(filename + " not found in directory. Please try again.")
    else:
        itemArray = []
        file_path = filename + ".txt"
        
        with open("./itemlists/" + file_path, 'r') as file:
            file_content = file.read()
        print("File content: " + file_content)

        #parse input to be readable inputs into values for object rankedItem
        file_content = file_content.strip("{}\'")
        file_content = file_content.replace("'", "")
        file_content = file_content.replace(":", "").replace(",", "").split()

        print("File content after strip: " + str(file_content))
        for i in range(0, len(file_content), 2):
            itemName = str(file_content[i])
            itemRank = int(file_content[i+1])
            item = classes.rankedItem(itemName, itemRank)
            itemArray.append(item)
            print("item: " + item.define())
    
    return itemArray

def testWriteToJson():
    print("testWriteToJson executed.")
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    return