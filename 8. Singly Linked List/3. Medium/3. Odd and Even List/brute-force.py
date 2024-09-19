from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = head
        values = []

        # Collecting values from odd-indexed nodes (1st, 3rd, 5th, ...)
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        temp = head.next

        # Collecting values from even-indexed nodes (2nd, 4th, 6th, ...)
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        # Assigning collected values back to the nodes
        index = 0
        temp = head
        while temp:
            temp.val = values[index]
            index += 1
            temp = temp.next

        return head
