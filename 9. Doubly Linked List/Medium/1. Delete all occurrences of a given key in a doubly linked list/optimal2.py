class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def deleteAllOccurrences(head: Node, k: int) -> Node:
    # Delete occurrences from the head
    while head and head.data == k:
        next_node = head.next
        if next_node:
            next_node.prev = None
        head = next_node

    current = head

    while current:
        if current.data == k:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        current = current.next

    return head
