class MyQueue:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def push(self, x: int) -> None:
        """Add an item to the rear of the queue."""
        self.enqueue_stack.append(x)

    def pop(self) -> int:
        if self.empty():
            raise IndexError("dequeue from empty queue")
        if not self.dequeue_stack:
            # Move all items from enqueue_stack to dequeue_stack, reversing their order
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self) -> int:
        if self.empty():
            raise IndexError("peek from empty queue")
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack[-1]

    def empty(self) -> bool:
        return not (self.enqueue_stack or self.dequeue_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
