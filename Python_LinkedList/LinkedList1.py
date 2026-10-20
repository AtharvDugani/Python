class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
a = Node(2)
b = Node(3)
c = Node(4)
a.next = b
b.next = c
head = a
# print(head.next.next.data)

def print_list(head):
    current = head
    while current != None:
        print(current.data, end=" ")
        current = current.next
print_list(head)
print()

# Inserting New Node at Beginning
NewNode = Node(5)
NewNode.next = head
head = NewNode
print_list(head)
print()

# Inserting New Node at end
NewNode = Node(10)
curr = head
while curr.next != None:
    curr = curr.next
curr.next = NewNode
print_list(head)
print()
# Inserting New Node at nth index

NewNode = Node(6)
n = 2
curr = head
for i in range(1, n-1):
    curr = curr.next
NewNode.next = curr.next.next 
curr.next = NewNode
print_list(head)
print()

# deleting the first node
head = head.next
print_list(head)
print()

# deleting last node
curr = head
while curr.next.next != None:
    curr =curr.next
curr.next = None
print_list(head)
print()

# deleting Nth node
n = 2
curr = head
for i in range(1,n-1):
    curr = curr.next
curr.next = curr.next.next
print_list(head)
print()

