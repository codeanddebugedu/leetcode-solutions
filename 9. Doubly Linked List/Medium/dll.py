class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertAtHead(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtTail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def traverse(self):
        if not self.head:
            print("DLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()


dll = DoublyLinkedList()
dll.insertAtHead(100)
dll.insertAtHead(200)
dll.insertAtHead(300)
dll.traverse()

"""
insertInBetween(2,987)
deleteHead()
deleteTail()
deleteByValue(500)
"""
