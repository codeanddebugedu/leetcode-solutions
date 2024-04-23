from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        """Pushes an item onto the stack."""
        # Enqueue the item
        self.queue.append(item)
        # Rotate the queue to make the newly added item at the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """Removes the item on top of the stack and returns it."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.queue.popleft()

    def peek(self):
        """Returns the top item of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.queue[0]

    def is_empty(self):
        """Returns True if the stack is empty, otherwise False."""
        return len(self.queue) == 0

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.queue)

    def __str__(self):
        """Provides a string representation of the stack."""
        return str(self.queue)


if __name__ == "__main__":
    stack = StackUsingQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack content = {stack}")
    print(f"Popped item = {stack.pop()}")
    print(f"Stack content = {stack}")
    print(f"Top item after pop = {stack.peek()}")
    print(f"Stack is empty = {stack.is_empty()}")
