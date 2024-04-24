from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        # Rotate the queue to make the newly added item at the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """Removes the item on top of the stack and returns it."""
        if self.empty():
            raise IndexError("pop from empty stack")
        return self.queue.popleft()

    def top(self) -> int:
        """Returns the top item of the stack without removing it."""
        if self.empty():
            raise IndexError("peek from empty stack")
        return self.queue[0]

    def empty(self) -> bool:
        """Returns True if the stack is empty, otherwise False."""
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
