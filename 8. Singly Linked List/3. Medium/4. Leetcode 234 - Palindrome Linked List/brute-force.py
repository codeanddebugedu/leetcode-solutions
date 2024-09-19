from typing import Optional

"""
Time complexity -> O(2N)
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp is not None:
            if temp.val != stack.pop():
                return False
            temp = temp.next
        return True
