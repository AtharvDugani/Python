class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack_operation:
    def __init__(self):
        self.top = None

    def push(self,data):
        NewNode = Node(data)
        NewNode.next = self.top
        self.top = NewNode

    def pop(self):
        if self.top is None:
            print("Stack underflow!!")
            return
        print("Poped element: ", self.top.data)
        self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack Underflow!!")
        else:
            print("Top element:",self.top.data)

    def printstack(self):
        curr = self.top
        while curr is not None:
            print(curr.data,end=" ")
            curr = curr.next
        print()

stack = Stack_operation()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.printstack()

stack.pop()
stack.pop()

stack.printstack()
stack.peek()




