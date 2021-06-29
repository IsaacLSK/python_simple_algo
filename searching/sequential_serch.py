
def sorted():
    numlist = [10, 5, 3, 15, 32, 20, 9, 6]
    numlist.sort()
    print("The minimum number is", numlist[0])
    print("The maximum number is", numlist[-1])

def nonSort():
    numlist = [10, 5, 3, 15, 32, 20, 9, 6]
    minimum = maximum = None
    for i in numlist:
        if minimum is None or i < minimum:
            minimum = i
        if maximum is None or i > maximum:
            maximum = i
    print("The minimum number is", minimum)
    print("The maximum number is", maximum)  

def searchlist(target):
    numlist = [10, 5, 3, 15, 32, 20, 9, 6]
    for i in numlist:
        if i == target: # if the target is found, stop looping
            print("The target ({}) is found".format(target))
            break
    else:
        print("Target not found")

if __name__ == "__main__":
    sorted()
    nonSort()
    searchlist(6) 
