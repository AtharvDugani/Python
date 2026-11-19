class Node:
    def __init__(self,value):
        self.left = None
        self.value = value
        self.right = None
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return            
        else:
            temp = self.root
            while True:
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right
    def inorder(self, temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.value, end=" ")
            self.inorder(temp.right)

    

BinarySearchTree = BST()
BinarySearchTree.insert(10)
BinarySearchTree.insert(5)
BinarySearchTree.insert(20)
BinarySearchTree.inorder(BinarySearchTree.root)
                    