import random
class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children

class BST:
    def __init__(self):
        self.root = None

    def setRoot(self,val):
        self.root = Node(val)

    def insert(self, val):
        #mutator method to add a node to the sree 
        if(self.root is None):
            self.setRoot(val)
        else:
            self.__insertNode(self.root, val)

    def __insertNode(self, currentNode, val):
        #private method to create a node
        if(val <= currentNode.getVal()):
            if(currentNode.leftChild):
                self.__insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.__insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        #accessor method to find and return a node's value
        return self.__findNode(self.root, val)

    def __findNode(self, currentNode, val):
        #private method to return the value from a node
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.__findNode(currentNode.leftChild, val)
        else:
            return self.__findNode(currentNode.rightChild, val)

#create a new emptry tree
tree = BST()
#create nodes 8 in the tree with values between 1 and 25
for i in range (1,9):
    tree.insert(random.randint(1,25))


#search the tree
for i in range(1,10):
    #check to see if there are nodes with values from 1 to 9 in the tree
    found = tree.find(i)
    print(i, found)
    
