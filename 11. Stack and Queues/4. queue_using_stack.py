class StackQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            print("Stack is empty")
            return -1  # Representing empty stack
        top_element = self.st1.pop()
        return top_element

    def peek(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        return self.st1[-1]

    def is_empty(self):
        return not self.st1


if __name__ == "__main__":
    q = StackQueue()

    # List of commands
    commands = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
    # List of inputs
    inputs = [[], [4], [8], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            q.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(q.pop(), end=" ")
        elif commands[i] == "peek":
            print(q.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if q.is_empty() else "false", end=" ")
        elif commands[i] == "StackQueue":
            print("null", end=" ")
