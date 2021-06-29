class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextobj = None

class LinkedList:
    def __init__(self):
       self.head = None # the head variable is set to None
    
    def insert(self, data): # insert new data at the front of linked list
        newnode = Node(data)
        newnode.nextobj = self.head
        self.head = newnode
    
    def print(self): # printing all nodes by traversal
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.nextobj

    def insertEnd(self, data): # insert new data at the end
        if self.head is None: # if linked list has no node
            self.head = Node(data) # simply add a new node
            return
        temp = self.head # traverse to the last node
        while temp.nextobj != None:
            temp = temp.nextobj
        # temp is now at last node
        temp.nextobj = Node(data)

    def delete(self, index): # index is the position of the target node
        if self.head is None:
            return
        if index < 0:
            raise IndexError("Attempt to use negative index")
        # first case
        temp = self.head
        if index == 0:
            self.head = temp.nextobj
            del temp
            return
        # second case
        while index > 0:
            ptr = temp
            temp = temp.nextobj
            index -= 1
        ptr.nextobj = temp.nextobj
        del temp

    def deleteNodeOfData(self, targetdata):
        if self.head is None:
            return
        # first case
        temp = self.head
        if temp.data == targetdata:
            self.head = temp.nextobj
            del temp
            return
        # second case
        while temp != None and temp.data != targetdata:
            ptr = temp
            temp = temp.nextobj
        if temp is None:
            return
        ptr.nextobj = temp.nextobj
        del temp

if __name__ == "__main__":
    print('\nlinkedlist #1')
    linkedlist = LinkedList()
    linkedlist.insert('Anders')
    linkedlist.insert('Betsy')
    linkedlist.insert('Chris')
    linkedlist.insertEnd('Isaac')
    linkedlist.print()

    print("\ndelete node based on index (#1) (Betsy):")
    linkedlist.delete(1)
    linkedlist.print()

    print('\nlinkedlist #2')
    linkedlist2 = LinkedList()
    linkedlist2.insert('Anders')
    linkedlist2.insert('Betsy')
    linkedlist2.insert('Chris')
    linkedlist2.insertEnd('Isaac')
    linkedlist2.print()
    print("\ndelete node based on data (Betsy):")
    linkedlist2.deleteNodeOfData('Betsy')
    linkedlist2.print()