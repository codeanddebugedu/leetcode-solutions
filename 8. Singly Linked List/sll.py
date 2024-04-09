class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # if self.head is None:
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next

    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            new_node.next = current
            # if prev_node is not None:
            prev_node.next = new_node


sll = SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(50)
sll.append(20)
sll.traverse()
print()
sll.insert_at(43, 0)
sll.traverse()
print()
sll.insert_at(400, 3)
sll.traverse()
