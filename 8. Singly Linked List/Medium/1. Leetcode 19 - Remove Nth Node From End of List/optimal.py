from typing import Optional

"""
Time complexity -> O(N)
O(N) since the fast pointer will traverse the entire linked list, 
where N is the length of the linked list.

Space complexity -> O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fastp = head
        slowp = head

        for _ in range(n):
            fastp = fastp.next

        if fastp is None:
            return head.next

        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next

        slowp.next = slowp.next.next
        return head
