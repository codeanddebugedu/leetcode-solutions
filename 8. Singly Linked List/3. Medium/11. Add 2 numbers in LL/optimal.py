from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode(0)
        temp = result
        carry = 0
        while (l1 != None and l2 != None) or carry:
            total = 0
            if l1 != None:
                total += l1.val
                l1 = l1.next
            if l2 != None:
                total += l2.val
                l2 = l2.next
            total += carry
            if total > 9:
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(total % 10)
            temp = temp.next
        return result.next
