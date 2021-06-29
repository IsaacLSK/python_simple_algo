class Stack:
    def __init__(self):
        self.data = list()  # create an empty list

    def push(self, value):
        self.data.append(value)
   
    def pop(self):
        if len(self.data) == 0:
            raise IndexError('Attempt to pop an empty stack')
        value = self.data.pop()  # from last index
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
    theStack = Stack()
    theStack.push(20)
    theStack.push(15)
    theStack.push(36)
    theStack.push(8)
    theStack.push(26)
    print("Content of the stack (top at the end): ", end='')
    theStack.print()

    while not theStack.isEmpty():
        print(theStack.pop())