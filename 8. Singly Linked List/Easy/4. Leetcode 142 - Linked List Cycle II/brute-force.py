from typing import Optional

"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(N)
The code uses a hashmap/dictionary/set to store encountered nodes, 
which can take up to O(N) additional space, 
where 'n' is the number of nodes in the list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_set = set()
        temp = head
        while temp is not None:
            if temp in my_set:
                return temp
            my_set.add(temp)
            temp = temp.next
        return None
