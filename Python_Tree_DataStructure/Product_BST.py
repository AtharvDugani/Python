
class Node:
    def __init__(self, pid):
        self.right = None
        self.pid = pid
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    # Insert product ID
    def insert(self, pid):
        new_node = Node(pid)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.pid < temp.pid:
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

    # Search product ID
    def search(self, root, pid):
        if root is None:
            return False

        if pid == root.pid:
            return True

        elif pid < root.pid:
            return self.search(root.left, pid)

        else:
            return self.search(root.right, pid)

    # Delete product ID
    def delete(self, root, pid):
        if root is None:
            return root

        if pid < root.pid:
            root.left = self.delete(root.left, pid)

        elif pid > root.pid:
            root.right = self.delete(root.right, pid)

        else:
            # Node has no left child
            if root.left is None:
                return root.right

            # Node has no right child
            if root.right is None:
                return root.left

            # Node has two children
            succ = self.get_successor(root)
            root.pid = succ.pid

            root.right = self.delete(root.right, succ.pid)

        return root

    # Find inorder successor
    def get_successor(self, root):
        temp = root.right

        while temp.left is not None:
            temp = temp.left

        return temp

    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.pid, end=" ")
            self.inorder(root.right)

    # Preorder traversal
    def preorder(self, root):
        if root:
            print(root.pid, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.pid, end=" ")

    # Find minimum product ID
    def find_min(self, root):
        if root is None:
            return None

        while root.left is not None:
            root = root.left

        return root.pid

    # Find maximum product ID
    def find_max(self, root):
        if root is None:
            return None

        while root.right is not None:
            root = root.right

        return root.pid


# Main program

bst = BST()

# 1. Insert product IDs
bst.insert(150)
bst.insert(100)
bst.insert(200)
bst.insert(75)
bst.insert(125)
bst.insert(175)
bst.insert(250)
bst.insert(60)
bst.insert(90)
bst.insert(110)

# 2. Display product IDs in ascending order
print("Product IDs in Ascending Order: ", end="")
bst.inorder(bst.root)

# 3. Search for product ID 175
num = int(input("\nEnter Product ID to find: "))

if bst.search(bst.root, num):
    print(f"{num} exists in Product IDs")
else:
    print(f"{num} does not exist in Product IDs")

# 4. Delete product ID 100
bst.root = bst.delete(bst.root, 100)

print("\nAfter deleting 100: ", end="")
bst.inorder(bst.root)

# 5. Display all traversals
print("\n\nInorder Traversal: ", end="")
bst.inorder(bst.root)

print("\nPreorder Traversal: ", end="")
bst.preorder(bst.root)

print("\nPostorder Traversal: ", end="")
bst.postorder(bst.root)

# 6. Find minimum and maximum product IDs
print("\n\nMaximum Product ID:", bst.find_max(bst.root))
print("Minimum Product ID:", bst.find_min(bst.root))
