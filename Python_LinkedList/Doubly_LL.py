class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        NewNode = Node(data)

        if self.head == None:
            self.head = NewNode
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = NewNode
        NewNode.prev = curr

    def insert(self, data, n):
        NewNode = Node(data)
        if n==1:
            NewNode.next = self.head
            if self.head is None:
                self.head.prev = NewNode
            
            self.head = NewNode
            return
        curr = self.head
        for i in range(1,n-1):
            curr = curr.next
        NewNode.next = curr.next
        NewNode.prev = curr
        if curr.next is not None:
            curr.next.prev = NewNode

        curr.next = NewNode
    def delete(self, n):
        curr = self.head
        if n == 1:
            self.head = curr.next

            if self.head is not None:
                self.head.prev = None
            return
        
        for i in range(1,n):
            curr = curr.next
        curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev

    def print_list(self):
        curr = self.head
        while curr != None:
            print(curr.data,end=" ")
            curr = curr.next
        print()
dll = LinkedList()
dll.append(10)
dll.append(20)
dll.print_list()        
dll.insert(9,1)
dll.insert(30,2)
dll.print_list()
dll.delete(2)
dll.print_list()