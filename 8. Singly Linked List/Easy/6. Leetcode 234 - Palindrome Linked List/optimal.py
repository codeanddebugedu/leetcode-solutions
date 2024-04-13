from typing import Optional

"""
Time complexity -> O(N/2+ N/2+ N/2+ N/2) -> O(2N)
N is the number of nodes

Space complexity -> O(N)
The code uses a stack to store encountered nodes
where 'n' is the number of nodes in the list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new_head = self.reverseList(slow.next)
        first = head
        second = new_head
        while second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        self.reverseList(new_head)
        return True
