class Node:
    def __init__(self,data):
        self.right = None
        self.data = data 
        self.left = None

class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.data < temp.data:
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
    def find_max(self):
        temp = self.root
        while temp.right :
            temp = temp.right
        return temp.data
    
    def find_min(self):
        temp = self.root
        while temp. left:
            temp = temp.left
        return temp.data
    
    def count_leaf_node(self, root):
        if root is None:
            return 0
        elif root.right is None and root.left is None:
            return 1
        return self.count_leaf_node(root.left) + self.count_leaf_node(root.right)
    
    def count_nonleaf_node(self, root):
        if root is None:
            return 0
        elif root.right is None and root.left is None:
            return 0
        return 1 + self.count_nonleaf_node(root.left) + self.count_nonleaf_node(root.right)
    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)    
    
bst = BST()
bst.insert(150)
bst.insert(100)
bst.insert(200)
bst.insert(75)
bst.insert(125)
bst.insert(175)
bst.insert(250)
bst.insert(60)
bst.insert(90)



print("Maximum Node:",bst.find_max())
print("Minimum Node: ",bst.find_min())

print("Leaf Node:",bst.count_leaf_node(bst.root))
print("Non Leaf Node: ", bst.count_nonleaf_node(bst.root))

print("Number of Node",bst.count_nodes(bst.root))
           