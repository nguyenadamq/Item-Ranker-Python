import classes

#loop user input
def loopUserInput(itemArray):
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

            #sort array after update with override
            itemArray = sort(itemArray)
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

#function to search for specific itemName within itemArray
def searchItem(itemArray, searchName):

    #iterate through array of items
    for i in range(len(itemArray)):
        if itemArray[i].name.lower() == searchName.lower():
            return i
    return -1

#if duplicate found then ask to overwrite or keep
def checkDuplicate(itemArray, searchName, n):
        
    #search for itemname
    n = searchItem(itemArray, searchName)

    #if found then return the information found
    if(n >= 0):
        print(f"The value of n: {n}")
        
        #located itemname
        print(f"The element '{searchName}' was found at index {n} (checkDuplicate)")
        print(itemArray[n].define())
        return True
    else:
        print(f"The element '{searchName}' was not found in the list")
        return False


#function to print all items in the array itemArray and their object values - calling the function "define()"
def printItems(itemArray):
    print(f"Here is the list of items that you entered: ")
    for i in range(len(itemArray)):
        print(itemArray[i].define())
    return None

#print the rankings(to test sort)
def printRankings(itemArray):
    for i in range(len(itemArray)):
        print(itemArray[i].rank, end = " ")
    print("\n")
    return None

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
