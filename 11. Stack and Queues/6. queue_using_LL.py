class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """Check if the queue is empty - O(1)"""
        return self.size == 0

    def enqueue(self, data):
        """Add an element to the back of the queue - O(1)"""
        new_node = Node(data)

        if self.is_empty():
            # If queue is empty, new node becomes both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Add new node at the tail (back of queue)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        """Remove and return the front element of the queue - O(1)"""
        if self.is_empty():
            raise Exception("Queue Underflow: Cannot dequeue from an empty queue")

        # Get the data from the head node (front of queue)
        data = self.head.data

        # If there's only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Move head pointer to next node
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return data

    def front(self):
        """Return the front element without removing it - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.head.data

    def rear(self):
        """Return the rear element without removing it - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.tail.data

    def get_size(self):
        """Return the number of elements in the queue - O(1)"""
        return self.size

    def display(self):
        """Display all elements in the queue - O(n)"""
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.head
        print("Queue (front to back):")
        while current:
            print(f"| {current.data} |", end=" ")
            current = current.next
        print("\n-----")


# Example usage
if __name__ == "__main__":
    queue = Queue()

    # Enqueue some elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    # Display queue
    queue.display()

    # Dequeue an element
    print(f"Dequeued: {queue.dequeue()}")

    # Look at front and rear elements
    print(f"Front element: {queue.front()}")
    print(f"Rear element: {queue.rear()}")

    # Get size
    print(f"Queue size: {queue.get_size()}")

    # Display queue after operations
    queue.display()

    # Dequeue remaining elements
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")

    # Check if empty
    print(f"Is queue empty? {queue.is_empty()}")

    # Try to dequeue from empty queue
    try:
        queue.dequeue()
    except Exception as e:
        print(f"Error: {e}")
