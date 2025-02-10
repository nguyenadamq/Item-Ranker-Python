import classes

def loopUserInput(itemArray):
    input = input("Would you like to add another item?(Y/y) or (N/n)")
    while input == 'y' or 'Y':
        itemName = input("What is the name of your item :")
        itemRank = input("What do you rank your item: ")
        itemArray.append()
        input = input("Would you like to add another item?(Y/y) or (N/n)")

    return itemArray
#function to search for specific itemName within itemArray
def searchItem(itemArray, itemName):
    target = itemName.lower()
    print(target)
    return None

#function to print all items in the array itemArray and their object values - calling the function "define()"
def printItems(itemArray):
    for i in range(len(itemArray)):
        print(itemArray[i].define())
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
        if classes.rankedItem.left[i].rank < classes.rankedItem.right[j].rank:
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

