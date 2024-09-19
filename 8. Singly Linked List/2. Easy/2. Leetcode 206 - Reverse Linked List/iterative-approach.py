from typing import Optional

"""
Time complexity -> O(N)
O(N) The code traverses the entire linked list once, 
where 'n' is the number of nodes in the list. 
This traversal has a linear time complexity, O(n).

Space complexity -> O(1)
The code uses only a constant amount of additional space, 
regardless of the linked list's length. 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
