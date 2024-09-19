class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Please do not change code above.


def deleteLast(list: Node) -> Node:
    head = list
    current_node = head
    prev = None
    while current_node.next:
        prev = current_node
        current_node = current_node.next
    prev.next = None
    return head
