from typing import Optional

"""
Time complexity -> O(N)
where 'n' is the number of nodes in the list. 

Space complexity -> O(1)
However, it's important to note that there is an implicit use of 
stack space due to recursion. 
This recursive stack space stores function calls and associated variables 
during the recursive traversal and reversal of the linked list. 
Despite this, no extra memory beyond the program's existing execution space is allocated, 
hence maintaining a space complexity of O(1).
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head
