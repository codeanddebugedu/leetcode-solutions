class Solution:
    def reverseDLL(self, head):
        if not head:
            return None

        stack = []
        current = head

        # First pass: push all node data onto stack
        while current:
            stack.append(current.data)
            current = current.next

        # Second pass: pop from stack to reassign data in reverse
        current = head
        while current:
            current.data = stack.pop()
            current = current.next

        return head
