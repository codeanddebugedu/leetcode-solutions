class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at Head
    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # 2. Insert at Last (Append)
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # 3. Insert in between (at a given position)
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    # 4. Delete Head Node
    def delete_head(self):
        if not self.head:
            print("List is empty!")
            return
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # 5. Delete Last Node
    def delete_last(self):
        if not self.head:
            print("List is empty!")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    # 6. Delete in between (at a given position)
    def delete_at(self, position):
        if not self.head:
            print("List is empty!")
            return
        if position == 0:
            self.delete_head()
            return
        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1
        if not current:
            print("Position out of bounds")
            return
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    # 7. Traverse Forward
    def traverse_forward(self):
        if not self.head:
            print("DLL is empty")
            return
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

    # 8. Traverse Backward
    def traverse_backward(self):
        if not self.head:
            print("DLL is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.val, end=" ")
            current = current.prev
        print()

    # 9. Search for an element
    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.val == key:
                print(f"Element {key} found at position {position}")
                return
            current = current.next
            position += 1
        print(f"Element {key} not found in the list")


# **Testing the DLL**
dll = DoublyLinkedList()

# Insert at head
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_head(30)

# Insert at last (append)
dll.append(40)
dll.append(50)

# Insert in between
dll.insert_at(25, 2)  # Insert 25 at index 2

# Traverse forward
print("Traverse forward:")
dll.traverse_forward()

# Traverse backward
print("Traverse backward:")
dll.traverse_backward()

# Delete head
dll.delete_head()
print("After deleting head:")
dll.traverse_forward()

# Delete last node
dll.delete_last()
print("After deleting last node:")
dll.traverse_forward()

# Delete in between
dll.delete_at(2)
print("After deleting node at position 2:")
dll.traverse_forward()

# Search for an element
dll.search(25)
dll.search(40)
