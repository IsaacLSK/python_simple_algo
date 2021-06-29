# Binary Search Tree Implementation
# with separated key and data

class Node:
    def __init__(self, key, data=None):
        self.key = key    # the key for BST
        self.data = data  # the payload
        self.left = None
        self.right = None

    def insert(self, key, data=None):
        if self.key is None:
            return
        if key < self.key:
            if self.left is None:
                self.left = Node(key, data)
            else:
                self.left.insert(key, data)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, data)
            else:
                self.right.insert(key, data)
        else:
            self.data = data # replace the data if duplicated key

    # searching for data based on key
    # return data
    def searchKey(self, key):
        if self.key is None:
            return None
        if key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.searchKey(key)            
        elif key > self.key:
            if self.right is None:
                return None
            else:
                return self.right.searchKey(key)
        else:
            return self.data  # the key is found
            
    # pre-order traversal
    def printPreOrder(self):
        print(self.key, self.data)
        if self.left:
            self.left.printPreOrder()
        if self.right:
            self.right.printPreOrder()
            
    # in-order traversal
    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.key, self.data)
        if self.right:
            self.right.printInOrder()

    # post-order traversal
    def printPostOrder(self):
        if self.left:
            self.left.printPostOrder()
        if self.right:
            self.right.printPostOrder()
        print(self.key, self.data)

    # returns the number of nodes
    def countNodes(self):
        count = 1
        if self.left:
            count += self.left.countNodes()
        if self.right:
            count += self.right.countNodes()
        return count

    # returns height of tree
    def treeHeight(self):
        leftheight = rightheight = 0
        if self.left:
            leftheight = self.left.treeHeight() + 1
        if self.right:
            rightheight = self.right.treeHeight() + 1
        return max(leftheight, rightheight)


class BSTree:
    def __init__(self):
        self.root = None  # link to root node

    def insert(self, key, data=None):
        if self.root is None:
            self.root = Node(key, data)
        else:
            self.root.insert(key, data)

    # searching for data based on key
    # return data
    def searchKey(self, key):
        if self.root:
            return self.root.searchKey(key)
        return None

    def printPreOrder(self):
        if self.root:
            self.root.printPreOrder()

    def printInOrder(self):
        if self.root:
            self.root.printInOrder()
            
    def printPostOrder(self):
        if self.root:
            self.root.printPostOrder()
            
    # returns the number of nodes
    def countNodes(self):
        if self.root:
            return self.root.countNodes()
        return 0

    # returns height of tree
    def treeHeight(self):
        if self.root:
            return self.root.treeHeight()
        return None  # height is None for empty tree        

if __name__ == "__main__":

    tree = BSTree()
    numlist = [34, 23, 4, 15, 28, 53, 38, 36, 72]
    for num in numlist:    # add numbers to the binary tree
        tree.insert(num)
    
    print('''
    The tree:

                 34
        23                  53
    4       28          38       72
      15             36
    ''')
    print("Pre-order traversal")
    tree.printPreOrder()    
    print("In-order traversal")
    tree.printInOrder()
    print("Post-order traversal")
    tree.printPostOrder()

    print("Number of nodes = ", tree.countNodes())
      
    print("Height of tree = ", tree.treeHeight())
