from typing import Optional

"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(N)
The code uses a hashmap/dictionary to store encountered nodes, 
which can take up to O(N) additional space, 
where 'n' is the number of nodes in the list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        node_set = set()
        while temp is not None:
            if temp in node_set:
                return True
            node_set.add(temp)
            temp = temp.next
        return False
