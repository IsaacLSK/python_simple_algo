class Queue:
    def __init__(self):
        self.data = list()  # create an empty list

    def enQueue(self, value):
        self.data.append(value)
    
    def deQueue(self):
        if len(self.data) == 0:
            raise IndexError('Attempt to deQueue an empty queue')
        value = self.data.pop(0)
        return value
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def isFull(self):
        return False
    
    def print(self, sep=','):
        isFirst = True
        for value in self.data:
            if not isFirst:
                print(sep, end='')
            print(value, end='')
            isFirst = False
        print()  # add a new line at the end

if __name__ == "__main__":
    theQueue = Queue()
    theQueue.enQueue(20)
    theQueue.enQueue(15)
    theQueue.enQueue(36)
    theQueue.enQueue(8)
    theQueue.enQueue(26)
    print("Content of the queue: ", end='')
    theQueue.print()
    
    while not theQueue.isEmpty():
        print(theQueue.deQueue())