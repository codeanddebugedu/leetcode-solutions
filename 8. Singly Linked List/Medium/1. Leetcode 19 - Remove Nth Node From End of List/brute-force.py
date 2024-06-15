from typing import Optional

"""
Time complexity -> O(L)+O(L-N)
We are calculating the length of the linked list and then 
iterating up to the (L-N)th node of the linked list, 
where L is the total length of the list.

Space complexity -> O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        length = 0
        current_node = head

        # Calculate the length of the linked list
        while current_node is not None:
            length += 1
            current_node = current_node.next

        # If the node to remove is the head of the list
        if length == n:
            new_head = head.next
            head = None
            return new_head

        # Find the node just before the one we want to remove
        position_to_stop = length - n
        current_node = head

        while current_node is not None:
            position_to_stop -= 1
            if position_to_stop == 0:
                break
            current_node = current_node.next

        # Remove the nth node from the end
        current_node.next = current_node.next.next
        return head
