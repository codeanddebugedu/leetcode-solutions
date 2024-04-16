class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(1)
"""


def deleteAllOccurrences(head: Node, k: int) -> Node:
    if not head.next and head.data == k:
        return None
    temp = head
    previous = None
    new_head = head
    while temp is not None:
        front = temp.next
        if temp.data == k:
            if previous:
                previous.next = temp.next
            if temp.next:
                temp.next.prev = previous
            if temp == new_head:
                new_head = new_head.next
        previous = temp
        temp = temp.next
    return new_head
