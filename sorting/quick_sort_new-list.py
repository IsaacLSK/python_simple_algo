# Quick sort (Ascending order)(New Lists)
def quickSortAsc(alist):
    size = len(alist)
    if size <= 1:
        return
    # create two new empty sub-lists
    smallList = list()
    largeList = list()
    # partitioning    
    pivot = alist[0]
    pivotcount = 1   # potentially more than 1 pivot
    for i in range(1, size):
        if alist[i] < pivot:
            smallList.append(alist[i])
        elif alist[i] > pivot:
            largeList.append(alist[i])
        else:
            pivotcount += 1
    # recursive call to quicksort
    # the two sub-lists
    quickSortAsc(smallList)
    quickSortAsc(largeList)
    # copy the results to the original list
    alist.clear()
    alist.extend(smallList)
    alist.extend([pivot] * pivotcount)
    alist.extend(largeList)
    # print(alist)


if __name__ == "__main__":
    numlist = [20, 14, 36, 8, 56, 49]
    quickSortAsc(numlist)
    print(numlist)

    numlist = [50, 25, 75, 12, 80, 20, 70, 2, 90, 11, 33, 99, 5, 28, 77, 12]
    quickSortAsc(numlist)
    print(numlist)    
    
