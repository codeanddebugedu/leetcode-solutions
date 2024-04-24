class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # Front of the queue
        self.tail = None  # Rear of the queue

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is not None:
            # There are elements in the queue
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            # This is the first element being added
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            print("Dequeue from empty queue")
            return
        removed_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            # Queue is now empty
            self.tail = None
        return removed_value

    def peek(self):
        if self.is_empty():
            print("Peek from empty queue")
            return
        return self.head.value

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
