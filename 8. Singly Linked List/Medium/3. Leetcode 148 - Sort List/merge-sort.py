# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getMiddle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow  # Slow pointer ends at the middle (or just before)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to simplify merging
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Append remaining elements from either list
        tail.next = l1 or l2
        return dummy.next  # Skip the initial dummy node

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # Base case: empty or single-node list
            return head

        # 1. Split the list into two halves
        mid = self.getMiddle(head)
        left = head
        right = mid.next
        mid.next = None  # Disconnect the two halves

        # 2. Recursively sort the two halves
        left = self.sortList(left)
        right = self.sortList(right)

        # 3. Merge the sorted halves
        return self.mergeTwoLists(left, right)
