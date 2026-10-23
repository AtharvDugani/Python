class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularSLL:
    def __init__(self):
        self.head = None
    def append(self, data):
        NewNode = Node(data)
        if self.head == None:
            self.head = NewNode
            NewNode.next = self.head
            return
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = NewNode
            NewNode.next = self.head
    def delete(self, data):
        if self.head is None:
            return
        
        curr = self.head
        # If the head node needs to be deleted
        if curr.data == data:
            if curr.next == self.head:
                self.head = None
                return

            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head
            return
        while curr.next != self.head:
            if curr.next.data == data:
                curr.next = curr.next.next
                return

            curr = curr.next


    def printList(self):
        curr = self.head
        while True:
            print(curr.data,end=" ")
            curr = curr.next
            if curr == self.head:
                break

        print()

CLL = CircularSLL()
CLL.append(10)
CLL.append(20)
CLL.append(30)
CLL.printList()

CLL.delete(30)
CLL.printList()