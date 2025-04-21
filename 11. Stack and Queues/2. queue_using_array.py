class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Cannt deque from empty queue")
            return
        x = self.items.pop(0)
        return x

    def front(self):
        if len(self.items) == 0:
            print("Cannot front, queue is empty")
            return
        return self.items[0]

    def rear(self):
        if len(self.items) == 0:
            print("Cannot rear, queue is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue content = {queue}")
    print(f"Dequeued item = {queue.dequeue()}")
    print(f"Queue content = {queue}")
