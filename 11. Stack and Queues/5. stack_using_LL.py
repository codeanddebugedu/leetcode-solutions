class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None  # This will point to the top of the stack

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point new node's next to the current top
        self.head = new_node  # Make new node the new top

    def pop(self):
        if self.is_empty():
            print("pop from empty stack")
            return
        popped_node = self.head
        self.head = self.head.next  # Move the head to the next node
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("peek from empty stack")
            return
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
