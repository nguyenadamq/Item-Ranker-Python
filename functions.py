import classes

#loop user input
def loopUserInput(itemArray):

    option = input("\nChoose an option below(lowercase accepted): " 
                 + "\n(A) Add items "
                 + "\n(P) Print items "
                 + "\n(PR) Print items with their rankings"
                 + "\n(U) Update items"
                 + "\n(R) Remove items"
                 + "\n(E) Exit program\n"
                 + ": ")

    option = option.lower()
    while option != "e":
        if not option:
            print("Invalid input. Please choose an option.")
            option = input("\nWould you like to continue adding?(Y/y) or (N/n): ")
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

        option = input("\nChoose an option below(lowercase accepted): " 
                 + "\n(A) Add items "
                 + "\n(P) Print items "
                 + "\n(PR) Print items with their rankings"
                 + "\n(U) Update items"
                 + "\n(R) Remove items"
                 + "\n(E) Exit program\n"
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
    #initial inputs
    itemName = input("\nWhat is the name of your item: ")
    while not itemName:
        print("Invalid input. Please enter a name for your item: ")
        itemName = input("\nWhat is the name of your item: ")

    #search item for checkDuplicate
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

    #move here is item wasnt ranked during override
    if ranked == False:
        #get and validate item rank
        itemRank = int(input("What do you rank your item(1-10): "))
        while (itemRank < 1) or (itemRank > 10):
            print("Invalid input. Please enter ranking between 1-10.")
            itemRank = int(input("What do you rank your item(1-10): "))

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
                    itemRank = int(input("What do you rank your item(1-10): "))
                    while (itemRank < 1) or (itemRank > 10):
                        print("Invalid input. Please enter ranking between 1-10.")
                        itemRank = int(input("What do you rank your item(1-10): "))
                    
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

            #move here is item wasnt ranked during override
            if ranked == False:
                #get and validate item rank
                itemRank = int(input("What do you rank your item(1-10): "))
                while (itemRank < 1) or (itemRank > 10):
                    print("Invalid input. Please enter ranking between 1-10.")
                    itemRank = int(input("What do you rank your item(1-10): "))
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
        print(f"Here is the list of items that you entered: ")
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
        print(f"Here is the list of items that you entered: ")
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

#if duplicate found then ask to overwrite or keep
def checkDuplicate(itemArray, searchName, n):
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

    #move here is item wasnt ranked during override
    if ranked == False:
        #get and validate item rank
        itemRank = int(input("What do you rank your item(1-10): "))
        while (itemRank < 1) or (itemRank > 10):
            print("Invalid input. Please enter ranking between 1-10.")
            itemRank = int(input("What do you rank your item(1-10): "))

        #initialize the item with the class
        item = classes.rankedItem(itemName, itemRank)

        #add the item to the list
        itemArray.append(item)

        #sort itemArray right after append
        itemArray = sort(itemArray)
    return

#UPDATE item
def overwrite(itemArray,n):
    #get and validate item rank (finishing user input for overwrite)
    itemRank = int(input("What do you rank your item(1-10): "))
    while (itemRank < 1) or (itemRank > 10):
        print("Invalid input. Please enter ranking between 1-10.")
        itemRank = int(input("What do you rank your item(1-10): "))
            
        item = classes.rankedItem(itemName, itemRank)
        itemArray[n] = item

        #sort array after update with override
        itemArray = sort(itemArray)
        print("Item has been successfully overwritten.")

#DELETE ITEM
def removeItems(itemArray):
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
        print(itemName + " not found in list.")

        #initial inputs
        itemName = input("\nWhat is the name of your item: ")

        #validate input to be not empty
        while not itemName:
            print("Invalid input. Please enter a name for your item: ")
            itemName = input("\nWhat is the name of your item: ")

        #find index then remove
        n = searchItem(itemArray, itemName)
    removedItem = itemArray.pop(n)

    print(removedItem.name + "has been removed")

    option = input("Would you like to remove another item(Y/y) or (N/n)")
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
            print(removedItem.name + "has been removed")
    return
def addFirstItem(itemArray):
    #initial inputs
    itemName = input("\nWhat is the name of your item: ")
    while not itemName:
        print("Invalid input. Please enter a name for your item: ")
        itemName = input("\nWhat is the name of your item: ")

    #get and validate item rank
    itemRank = int(input("What do you rank your item(1-10): "))
    while (itemRank < 1) or (itemRank > 10):
        print("Invalid input. Please enter ranking between 1-10.")
        itemRank = int(input("What do you rank your item(1-10): "))

        #initialize the item with the class
        item = classes.rankedItem(itemName, itemRank)

        #add the item to the list
        itemArray.append(item)
    return itemArray