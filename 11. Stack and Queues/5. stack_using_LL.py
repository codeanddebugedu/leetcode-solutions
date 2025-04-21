class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """Check if the stack is empty - O(1)"""
        return self.size == 0

    def push(self, data):
        """Add an element to the top of the stack - O(1)"""
        new_node = Node(data)

        if self.is_empty():
            # If stack is empty, new node becomes both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Add new node at the tail (top of stack)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pop(self):
        """Remove and return the top element of the stack - O(1)"""
        if self.is_empty():
            raise Exception("Stack Underflow: Cannot pop from an empty stack")

        # Get the data from the tail node
        data = self.tail.data

        # If there's only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Move tail pointer to previous node
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return data

    def peek(self):
        """Return the top element without removing it - O(1)"""
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.tail.data

    def get_size(self):
        """Return the number of elements in the stack - O(1)"""
        return self.size

    def display(self):
        """Display all elements in the stack - O(n)"""
        if self.is_empty():
            print("Stack is empty")
            return

        current = self.tail
        print("Stack (top to bottom):")
        while current:
            print(f"| {current.data} |")
            current = current.prev
        print("-----")


# Example usage
if __name__ == "__main__":
    stack = Stack()

    # Push some elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    # Display stack
    stack.display()

    # Pop an element
    print(f"Popped: {stack.pop()}")

    # Peek at top element
    print(f"Top element: {stack.peek()}")

    # Get size
    print(f"Stack size: {stack.get_size()}")

    # Display stack after operations
    stack.display()

    # Pop remaining elements
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")

    # Check if empty
    print(f"Is stack empty? {stack.is_empty()}")

    # Try to pop from empty stack
    try:
        stack.pop()
    except Exception as e:
        print(f"Error: {e}")
