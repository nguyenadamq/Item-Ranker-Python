import classes

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
                 + "\n(E)  Exit program\n"
                 + ": ")

    option = option.lower()
    while option != "e":
        if not option:
            print("Invalid input. Please choose an option.")
        
        elif option == "a":
            #Start getting user input
            itemArray = addItem(itemArray)
            
        #Fix this to only print item names
        elif option == "p":
            n = 0
            printItems(itemArray, n)
        elif option == "pr":
            n = 1
            printItems(itemArray, n)
        elif option == "u":
            itemArray = updateItems(itemArray)
        elif option == "r":
            itemArray = removeItems(itemArray)
        elif option == "w":
            filenum = writeToFile(itemArray, filenum)
        else:
            print("Invalid choice. Please try again.")

        option = input("\nChoose an option below(lowercase accepted): " 
                 + "\n(A)  Add items "
                 + "\n(P)  Print items "
                 + "\n(PR) Print items with their rankings"
                 + "\n(U)  Update items"
                 + "\n(R)  Remove items"
                 + "\n(W)  Write to file"
                 + "\n(E)  Exit program\n"
                 + ": ")
        option = option.lower()
    return itemArray

#function to run merge sort of itemRanks within itemArray
def sort(itemArray):
    if len(itemArray) <= 1:
        return itemArray
    
    #initialize middle point
    mid = len(itemArray) // 2

    #Recursively check each side
    left_side = sort(itemArray[:mid])

    right_side = sort(itemArray[mid:])


    return merge(left_side, right_side)

#mergesort helper function
def merge(left, right):
    output = []
    i = 0
    j = 0

    #loop until all numbers are checked
    while i < len(left) and j < len(right):
        if left[i].rank < right[j].rank:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    #include end of partitions
    output.extend(left[i:])
    output.extend(right[j:])

    #return output
    return output

#CREATE item
def addItem(itemArray):
    n = -1
    #initial inputs
    itemName = input("\nWhat is the name of your item: ")
    while not itemName:
        print("Invalid input. Please enter a name for your item.")
        itemName = input("\nWhat is the name of your item: ")
        
    print("Current itemArray length: " + str(len(itemArray)))

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
        print(f"Here is the list of items: ")
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
        print(f"Here is the list of items: ")
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
    overwrite(itemArray, itemName, n)

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
        
        overwrite(itemArray, itemName, n)
                
        option = input("Would you like to update another item?(Y/y) (N/n): ")
        option.lower()

    #return updated array
    return itemArray

def arrayToString(itemArray):
    sentence = "Here is the list of items: "
    for i in range(len(itemArray)):
        sentence += itemArray[i].name + " "
    return sentence

def writeToFile(itemArray, filenum):
    sentence = arrayToString(itemArray)
    f = open("itemlist" + str(filenum) + ".txt", "w")
    f.write(sentence)

    #increment f for new item file for next time
    filenum = filenum + 1
    return filenum