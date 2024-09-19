from typing import Optional

"""
Time complexity -> O(N) + O(NlogN) + O(N)
Space complexity -> O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current_node = head

        # Collect all values from the linked list
        while current_node:
            values.append(current_node.val)
            current_node = current_node.next

        # Sort the values
        values.sort()

        # Reassign the sorted values to the linked list nodes
        current_node = head
        index = 0
        while current_node:
            current_node.val = values[index]
            index += 1
            current_node = current_node.next

        return head
