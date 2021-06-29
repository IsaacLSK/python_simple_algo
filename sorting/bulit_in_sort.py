def built_in_sort():

    # using the function sorted
    # the function returns the sorted list
    listA = [10, 5, 2, 8, 3, 4, 9, 1]
    newlist = sorted(listA)
    print(newlist)

    # using the function sorted
    # the function returns the sorted list
    listA = [10, 5, 2, 8, 3, 4, 9, 1]
    newlist = sorted(listA, reverse=True)
    print(newlist)

    # using the sort() method of list object directly
    # NOTE: the method directly sorts the list object
    listA = [10, 5, 2, 8, 3, 4, 9, 1]
    listA.sort()
    print(listA)
    
if __name__ == "__main__":
    built_in_sort()