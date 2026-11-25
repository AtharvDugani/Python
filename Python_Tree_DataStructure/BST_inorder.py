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
    def delete(self, root, value):
        if root is None:
            return None
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ = self.get_successor(root)
            root.value = succ.value
            root.right = self.delete(root.right, succ.value)
        return root
    def get_successor(self, root):
        temp = root.right
        while temp.left is not None :
            temp = temp.left
        return temp
    def search(self, root, value):
        if root is None:
            return False
        if value == root.value:
            return True
        elif value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)
        
    def inorder(self, temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.value, end=" ")
            self.inorder(temp.right)
    def preorder(self, temp):
        if temp is not None:
            print(temp.value,end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)
    def postorder(self, temp):
        if temp is not None:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.value, end=" ")

    

BinarySearchTree = BST()
BinarySearchTree.insert(10)
BinarySearchTree.insert(5)
BinarySearchTree.insert(20)
BinarySearchTree.insert(25)
BinarySearchTree.insert(50)
BinarySearchTree.insert(8)

print("Inorder: ",end="")
BinarySearchTree.inorder(BinarySearchTree.root)
print("\nPreorder: ",end="")
BinarySearchTree.preorder(BinarySearchTree.root)
print("\nPostorder: ",end="")
BinarySearchTree.postorder(BinarySearchTree.root)

print("\nDoes 55 exists: ",BinarySearchTree.search(BinarySearchTree.root, 55))    

print("Removed element 8: ",end="")
BinarySearchTree.delete(BinarySearchTree.root, 8)
BinarySearchTree.inorder(BinarySearchTree.root)