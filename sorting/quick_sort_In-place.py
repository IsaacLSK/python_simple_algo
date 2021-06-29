# Quick sort (Ascending order)(In-place)
def quickSortInplaceAsc(alist):
    # create a temp list of sufficient size
    templist = [0] * len(alist)
    # start quicksort in another function
    quickSortInplaceHandle(alist, 0, len(alist) - 1, templist)

def quickSortInplaceHandle(alist, left, right, templist):
    if right <= left:
        return
    # partitioning
    pivotIndex = quickSortPartition(alist, left, right, templist)
    # recursive calls
    quickSortInplaceHandle(alist, left, pivotIndex - 1, templist)
    quickSortInplaceHandle(alist, pivotIndex + 1, right, templist)    

# perform in-place partitioning of alist with the help
# of templist
def quickSortPartition(alist, left, right, templist):
    # parameters
    smallCount = 0   # number of data smaller than pivot
    largeCount = 0   # number of data larger than pivot
    pivot = alist[left]
    pivotcount = 1
    # partitioning
    for i in range(left + 1, right+1):
        if alist[i] < pivot:
            templist[left + smallCount] = alist[i]
            smallCount += 1
        elif alist[i] > pivot:
            templist[right - largeCount] = alist[i]
            largeCount += 1
        else:
            pivotcount += 1
    # add back the pivot
    # for loop needed because pivot may be more than 1
    for i in range(left + smallCount, right - largeCount + 1):
        templist[i] = pivot
    # copy back to original list
    for i in range(left, right + 1):
        alist[i] = templist[i]
    return left + smallCount


if __name__ == "__main__":
    numlist = [20, 14, 36, 8, 56, 49]
    quickSortInplaceAsc(numlist)
    print(numlist)

    numlist = [50, 25, 75, 12, 80, 20, 70, 2, 90, 11, 33, 99, 5, 28, 77, 12]
    quickSortInplaceAsc(numlist)
    print(numlist)    
    
