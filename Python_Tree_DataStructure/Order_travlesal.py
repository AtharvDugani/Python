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
    

    def level_order(self, root):
        if root is None:
            print("BST is empty!")
            return 
        arr = [] # initialize the array
        level = 0
        count = 0 # for counting visited Node
        arr.append(root)
        while count < len(arr):
            node_counter = len(arr) - count
            print("\n level: ", level,end=" ")
            for i in range(node_counter):
                temp = arr[count] # access the node in the array using count
                count += 1 # increment the counter
                print(temp.value,end=" ")
                # check whether the curruent node has left or right node
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level += 1
    def inorder(self, temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.value, end=" ")
            self.inorder(temp.right)
    

    

BinarySearchTree = BST()
BinarySearchTree.insert(10)
BinarySearchTree.insert(5)
BinarySearchTree.insert(20)
BinarySearchTree.insert(25)
BinarySearchTree.insert(50)
BinarySearchTree.insert(8)
BinarySearchTree.insert(44)
BinarySearchTree.insert(23)


print("Data in Asecing order: ")
BinarySearchTree.inorder(BinarySearchTree.root)
print()
BinarySearchTree.level_order(BinarySearchTree.root)