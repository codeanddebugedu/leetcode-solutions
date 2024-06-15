from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        # Calculate the length of the linked list
        temp = head
        length = 1
        while temp.next is not None:
            length += 1
            temp = temp.next

        # Connect the last node to the head to make it circular
        temp.next = head

        # Calculate the effective rotations needed as k might be greater than length
        k = k % length
        steps_to_new_head = length - k  # Find the position of the new head

        # Traverse to the new end of the list
        for _ in range(steps_to_new_head):
            temp = temp.next
            steps_to_new_head -= 1

        # Set the new head and break the circular link
        head = temp.next
        temp.next = None

        return head
