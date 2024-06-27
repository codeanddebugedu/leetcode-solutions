"""
Time Complexity: O(2N) The time complexity consists of actions of reversing segments of K 
and finding the Kth node which operates in linear time. 
Thus, O(N) + O(N) = O(2N), which simplifies to O(N).

Space Complexity: O(1) The space complexity is O(1) as the algorithm operates
in place without any additional space requirements.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head):
        # Set 'temp' to point to the head of the list
        temp = head
        # 'previous' will be used to track the prior node, initially set to None
        previous = None

        while temp is not None:
            # 'next_node' holds the reference to the next node in the list
            next_node = temp.next
            # Reverse the link so that the current node points to 'previous'
            temp.next = previous
            # Move 'previous' up to the current node
            previous = temp
            # Move 'temp' up to the next node in the original list
            temp = next_node

        # Return the new head of the reversed list
        return previous

    # Function to find the Kth node starting from a given node in the list
    def findKthNode(self, node, k):
        # Reduce k by 1 because we count from the first node
        k -= 1

        # Continue moving forward until we reach the Kth node or the end of the list
        while node is not None and k > 0:
            # Decrease k with each node we traverse
            k -= 1
            # Move to the next node
            node = node.next

        # Return the Kth node or None if we reached the end before finding it
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevGroupLastNode = None

        while temp is not None:
            kThNode = self.findKthNode(temp, k)
            if kThNode is None:
                if prevGroupLastNode:
                    prevGroupLastNode.next = temp
                break
            nextGroupFirstNode = kThNode.next
            kThNode.next = None
            self.reverseLinkedList(temp)
            if temp == head:
                head = kThNode
            else:
                prevGroupLastNode.next = kThNode
            prevGroupLastNode = temp
            temp = nextGroupFirstNode

        return head
