# This calss defines what is in the node or Structure of the node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    # For inititalizing the class
    def __init__(self):
        self.head = None

    # For Appending the data at the end
    def append(self, data):
        NewNode = Node(data)
        if self.head == None:
            self.head = NewNode
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = NewNode

    # for inserting the data at given position
    def insert(self, data, n):
        NewNode = Node(data)
        if n==1:
            NewNode.next = self.head
            self.head = NewNode
            return
        
        curr = self.head
        for i in range(1, n-1):
            curr = curr.next
        NewNode.next = curr.next
        curr.next = NewNode
        

    def delete(self, data):
        curr = self.head
        if curr != None and curr.data == data:
            self.head = curr.next
            return
        while curr != None and curr.next != None:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next
    def search_element(self, data):
        curr = self.head
        while curr != None:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    
    def sort_list(self):
        curr = self.head
        while curr != None:
            temp = curr.next
            while temp != None:
                if curr.data > temp.data:
                    curr.data, temp.data = temp.data, curr.data
                temp = temp.next
            curr = curr.next
            
    def print_list(self):
        curr = self.head
        while curr != None:
            print(curr.data,end=" ")
            curr = curr.next
        print()

list = LinkedList()

list.append(10)
list.append(20)
list.append(30)
list.print_list()

list.insert(40, 3)
list.insert(25,3)
list.print_list()

print(list.search_element(20))
print("Before: ")
list.print_list()
list.sort_list()
print("After:")
list.print_list()