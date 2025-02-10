import classes

def loopUserInput(itemArray):
    itemName = input("\nWhat is the name of your item :")
    itemRank = int(input("What do you rank your item(1-10): "))
    item = classes.rankedItem(itemName, itemRank)
    itemArray.append(item)
    while True:
        test = input("\nWould you like to add another item?(Y/y) or (N/n): ")
        if str(test).lower() == "y":
            itemName = input("What is the name of your item :")
            itemRank = int(input("What do you rank your item(1-10): "))
            while (itemRank < 1) or (itemRank > 10):
                print("Invalid input. Please enter ranking between 1-10.")
                itemRank = int(input("What do you rank your item(1-10): "))
            item = classes.rankedItem(itemName, itemRank)
            itemArray.append(item)
        elif str(test).lower() == "n":
            break
        else:
            print("Invalid input. Please try again.")

    return itemArray

#function to search for specific itemName within itemArray
def searchItem(itemArray, searchName, n):
    #iterate through array of items
    for i in range(len(itemArray)):
        if itemArray[i].itemName == searchName:

            return True
    return False

#function to print all items in the array itemArray and their object values - calling the function "define()"
def printItems(itemArray):
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

