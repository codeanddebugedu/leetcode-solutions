from typing import Optional

"""
Time complexity -> O(N + N/2)
N is the number of nodes

Space complexity -> O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        temp = head
        for i in range(n // 2):
            temp = temp.next
        return temp
