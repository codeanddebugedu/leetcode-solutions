from typing import Optional

"""
Time complexity -> O(2N) -> O(N)
N is the number of nodes

Space complexity -> O(N)
We use a stack to store the values of the linked list, and in the worst case, 
the stack will have all N values,  ie. storing the complete linked list. 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        temp = head

        while temp is not None:
            temp.val = stack.pop()
            temp = temp.next

        return head
