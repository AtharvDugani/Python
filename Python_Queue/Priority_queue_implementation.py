class Patient:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class Hospital:
    def __init__(self):
        self.front = None

    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            return

        if self.front.priority > new_node.priority:
                    new_node.next = self.front
                    self.front = new_node
                    return
        temp = self.front
        while temp.next != None and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        

    def display_next(self):
        if self.front == None:
            print("Queue is empty")
        else:
            print("Next Patient:", self.front.name)

    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Treated Patient:", temp.name)
            self.front = self.front.next

    def display_all(self):
        if self.front == None:
            print("Queue is empty")
            return

        temp = self.front

        while temp != None:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next


# Main Program
h = Hospital()

h.enqueue(Patient(101, "Akshay", 1))
h.enqueue(Patient(102, "Sonal", 2))
h.enqueue(Patient(103, "Vansh", 2))
h.enqueue(Patient(104, "Tanaya", 1))
h.enqueue(Patient(105, "Sanjana", 3))


print("All Waiting Patients:")
h.display_all()


h.display_next()

print("\nAfter Treatment:")
h.dequeue()
h.dequeue()

print("\nRemaining Patients:")
h.display_all()