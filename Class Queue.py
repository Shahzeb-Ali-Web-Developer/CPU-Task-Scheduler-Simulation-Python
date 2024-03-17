class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def peek(self):
        if not self.empty():
            return self.items[0]
        else:
            print("Queue is empty. Cannot peek.")
            return None

    def size(self):
        return len(self.items)

    def display(self):
        print("Current queue:")
        print(self.items)

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()  # Output: [1, 2, 3]

print("Peek:", queue.peek())  # Output: Peek: 1

print("Dequeue:", queue.dequeue())    # Output: Dequeue: 1

queue.display()  # Output: [2, 3]
