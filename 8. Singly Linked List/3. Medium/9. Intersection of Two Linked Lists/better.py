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
        lenA = 0
        lenB = 0
        lastNodeofA = None
        lastNodeofB = None
        temp = headA
        while temp:
            lenA += 1
            if temp.next is None:
                lastNodeofA = temp
            temp = temp.next
        temp = headB
        while temp:
            lenB += 1
            if temp.next is None:
                lastNodeofB = temp
            temp = temp.next
        if lastNodeofA is not lastNodeofB:
            return None
        diff = abs(lenA - lenB)
        if lenA > lenB:
            temp = headA
            while diff > 0:
                temp = temp.next
                diff -= 1
            while temp:
                if temp is headB:
                    return temp
                temp = temp.next
                headB = headB.next
        elif lenB > lenA:
            temp = headB
            while diff > 0:
                temp = temp.next
                diff -= 1
            while temp:
                if temp is headA:
                    return temp
                temp = temp.next
                headA = headA.next
        else:
            temp = headA
            while temp:
                if temp is headB:
                    return temp
                temp = temp.next
                headB = headB.next
