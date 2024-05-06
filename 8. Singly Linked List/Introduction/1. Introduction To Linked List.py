class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    n = len(arr)
    new_head = Node(arr[0])
    current_node = new_head
    for i in range(1, n):
        new_node = Node(arr[i])
        current_node.next = new_node
        current_node = new_node
    return new_head
