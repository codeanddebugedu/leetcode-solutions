from typing import Optional

"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(1)
The code uses only a constantamount of additionalspace, 
regardless of the linked list's length.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
