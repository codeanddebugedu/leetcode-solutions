class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue. Raise exception if the queue is empty."""
        if self.is_empty():
            print("dequeue from empty queue")
            return
        return self.items.pop(0)  # pop from the front of the list

    def peek(self):
        """Return the front item of the queue without removing it. Raise exception if the queue is empty."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the queue."""
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue content = {queue}")
    print(f"Dequeued item = {queue.dequeue()}")
    print(f"Queue content = {queue}")
