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
        all_nodes = set()
        temp = headA
        while temp:
            all_nodes.add(temp)
            temp = temp.next

        temp = headB
        while temp:
            if temp in all_nodes:
                return temp
            temp = temp.next
        return None
