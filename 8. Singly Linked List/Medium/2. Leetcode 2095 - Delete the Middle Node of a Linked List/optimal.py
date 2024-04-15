from typing import Optional

"""
Time complexity -> O(N/2)
Space complexity -> O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Tortoise Hare Approach (slightly changed)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow = head
        fast = head
        fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
