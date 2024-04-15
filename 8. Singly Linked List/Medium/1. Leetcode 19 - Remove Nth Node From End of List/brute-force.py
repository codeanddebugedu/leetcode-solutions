from typing import Optional

"""
Time complexity -> O(L)+O(L-N)
We are calculating the length of the linked list and then 
iterating up to the (L-N)th node of the linked list, 
where L is the total length of the list.

Space complexity -> O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        cnt = 0
        temp = head

        while temp is not None:
            cnt += 1
            temp = temp.next

        if cnt == n:
            newhead = head.next
            head = None
            return newhead

        res = cnt - n
        temp = head

        while temp is not None:
            res -= 1
            if res == 0:
                break
            temp = temp.next

        delNode = temp.next
        temp.next = temp.next.next
        delNode = None
        return head
