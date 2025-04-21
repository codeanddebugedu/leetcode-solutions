from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue.popleft()

    def peek(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


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
