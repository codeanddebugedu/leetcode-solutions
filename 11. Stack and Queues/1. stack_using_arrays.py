class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack. Raise exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item of the stack without removing it. Raise exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print(f"Stack content = {stack}")
    print(f"Popped item = {stack.pop()}")
    print(f"Stack content = {stack}")
    print(f"Top item after pop = {stack.peek()}")
    print(f"Stack is empty = {stack.is_empty()}")
