import random
    
def genlist(size):
    # generate numbers in the list in the range 10 times the size
    # if the size is 1000, it select 1000 integers from 0 to 10000 - 1
    return random.sample(range(0, size * 10), size)

# this function returns the index where the target is found in the list
# returns None if the target is not found
# numlist MUST BE SORTED
def binarySearch(numlist, target):
    size = len(numlist)
    lower = 0
    upper = size - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if target == numlist[middle]:
            return middle
        elif target > numlist[middle]:
            lower = middle + 1
        else:
            upper = middle - 1
    return None
    

if __name__ == "__main__":

    dataSize = 100
    numlist = genlist(dataSize)
    
    # sort the list
    numlist.sort()
    
    # draw a random nunmber from 0 to dataSize-1 as the target
    target = random.randrange(0, dataSize)
    index = binarySearch(numlist, target)
    print("The target {} is found at index {} in the list".format(target, index))

    # draw a nunmber randomly from numlist as the target
    target = random.choice(numlist)
    index = binarySearch(numlist, target)
    print("The target {} is found at index {} in the list".format(target, index))   

