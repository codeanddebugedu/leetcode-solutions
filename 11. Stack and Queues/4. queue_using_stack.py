class QueueUsingStacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.enqueue_stack.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        if not self.dequeue_stack:
            # Move all items from enqueue_stack to dequeue_stack, reversing their order
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self):
        """Return the front item of the queue without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack[-1]

    def is_empty(self):
        """Check if the queue is empty."""
        return not (self.enqueue_stack or self.dequeue_stack)

    def size(self):
        """Return the number of items in the queue."""
        return len(self.enqueue_stack) + len(self.dequeue_stack)

    def __str__(self):
        """Return a string representation of the queue for debugging."""
        if not self.dequeue_stack:
            return str(self.enqueue_stack[::-1])
        if not self.enqueue_stack:
            return str(self.dequeue_stack)
        return str(self.dequeue_stack + self.enqueue_stack[::-1])


if __name__ == "__main__":
    queue = QueueUsingStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue content = {queue}")
    print(f"Dequeued item = {queue.dequeue()}")
    print(f"Queue content = {queue}")
    print(f"Front item after dequeue = {queue.peek()}")
    print(f"Queue is empty = {queue.is_empty()}")
