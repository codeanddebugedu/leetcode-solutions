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


def removeDuplicates(self, head):
    cur = head
    while cur:
        if cur.prev and cur.prev.data == cur.data:
            if cur.prev == head:
                cur.prev = None
                head = cur
            else:
                cur.prev.prev.next = cur
                cur.prev = cur.prev.prev

        cur = cur.next
    return head
