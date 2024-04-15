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
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()

        temp = head
        index = 0
        while temp:
            temp.val = arr[index]
            index += 1
            temp = temp.next
        return head
