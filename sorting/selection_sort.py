# Selection sort (Ascending order)
def sortSelectionAsc():
    alist = [10, 5, 2, 8, 3, 4, 9, 1]
    size = len(alist)
    # unsortedEnd runs from size-1 to 1
    for unsortedEnd in range(size - 1, 0, -1):
        # search for largest value in unsorted part
        lindex = 0 # index of largest value
        for i in range(1, unsortedEnd + 1):
            if alist[i] > alist[lindex]: # if dec, change to <
                lindex = i
        # swap largest with end
        alist[lindex], alist[unsortedEnd] = alist[unsortedEnd], alist[lindex]
        print(alist) # print intermediate steps

if __name__ == "__main__":

    sortSelectionAsc()