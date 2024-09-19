"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(1)
"""


class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count = 1
            while slow is not fast:
                count += 1
                slow = slow.next
            return count
    return 0
