class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front
        else:
            self.rear.next = new_node
            new_node.next = self.front
            self.rear = new_node

    def dequeue(self):
        if self.empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        elif self.front == self.rear:
            item = self.front.data
            self.front = None
            self.rear = None
        else:
            item = self.front.data
            self.front = self.front.next
            self.rear.next = self.front
        return item

    def peek(self):
        if self.empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def empty(self):
        return self.front is None

    def display(self):
        if self.empty():
            print("Queue is empty.")
            return
        temp = self.front
        while temp.next != self.front:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)


# Example usage:
cq = CircularQueue()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.display()  # Output: 1 2 3 4
cq.dequeue()
cq.enqueue(5)
cq.display()  # Output: 2 3 4 5
