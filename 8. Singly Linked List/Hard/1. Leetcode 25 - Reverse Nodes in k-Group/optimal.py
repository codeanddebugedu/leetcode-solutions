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
        # 'temp' is used to traverse the list
        temp = head

        # 'prevGroupLastNode' keeps track of the last node of the previous reversed group
        prevGroupLastNode = None

        # Loop through the entire list
        while temp is not None:
            # Find the Kth node from the current node
            kThNode = self.findKthNode(temp, k)

            # If the Kth node does not exist, we have less than k nodes left
            if kThNode is None:
                # If there was a previous group, connect its last node to the current node
                if prevGroupLastNode:
                    prevGroupLastNode.next = temp

                # Exit the loop as we can't form another full group
                break

            # 'nextGroupFirstNode' holds the node after the Kth node
            nextGroupFirstNode = kThNode.next

            # Disconnect the Kth node to prepare for reversing the group
            kThNode.next = None

            # Reverse the current group of nodes
            self.reverseLinkedList(temp)

            # Update the head of the list if we're reversing the first group
            if temp == head:
                head = kThNode
            else:
                # Connect the last node of the previous group to the first node of the reversed group
                prevGroupLastNode.next = kThNode

            # Update 'prevGroupLastNode' to the last node of the current group
            prevGroupLastNode = temp

            # Move 'temp' to the start of the next group
            temp = nextGroupFirstNode

        # Return the head of the new list
        return head
