from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        temp1, temp2 = headA, headB

        while temp1 != temp2:
            if temp1 is not None:
                temp1 = temp1.next
            else:
                temp1 = headB
            if temp2 is not None:
                temp2 = temp2.next
            else:
                temp2 = headA

        return temp1
