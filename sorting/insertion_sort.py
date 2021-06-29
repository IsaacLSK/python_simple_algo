# Insertion sort (Ascending order)
def sortInsertionAsc():
    alist = [2,8,6,4,7,2,5,4,10,6,9]
    size = len(alist)
    # sortedEnd runs from 0 to size-1
    for sortedEnd in range(0, size):
        toInsert = alist[sortedEnd]
        # find suitable place to insert
        insertLoc = 0
        while insertLoc < sortedEnd:
            if toInsert < alist[insertLoc]: # if desc, change to >
                break
            insertLoc += 1
        # insertLoc is the location to insert
        # right shift the remainng elements in the sorted part
        for i in range(sortedEnd, insertLoc, -1):
            alist[i] = alist[i-1]
        alist[insertLoc] = toInsert
        print(alist)

if __name__ == "__main__":
    sortInsertionAsc()