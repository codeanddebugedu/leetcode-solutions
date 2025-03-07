class Solution:
    def reverseDLL(self, head):
        # Edge cases: if list is empty or has one node, just return head
        if not head or not head.next:
            return head

        prev = None
        current = head

        # Traverse through the list
        while current:
            # Store the next node
            front = current.next

            # Reverse current node's pointers
            current.next = prev
            current.prev = front

            # Move the prev pointer forward (to current)
            prev = current

            # Move current pointer to the originally 'next' node
            current = front

        # 'prev' will be pointing to the new head of the reversed list
        return prev
