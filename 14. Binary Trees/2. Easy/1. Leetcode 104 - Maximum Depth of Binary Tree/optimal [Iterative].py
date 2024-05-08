"""
Time Complexity: O(N) 
where N is the number of nodes in the Binary Tree. 
This complexity arises from visiting each node exactly once during the 
traversal to determine the maximum depth.

Space Complexity: O(N) 
where N is the number of nodes in the Binary Tree because in the 
worst case scenario the tree is balanced and has N/2 nodes in its last level 
which will have to be stored in the queue.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        height = 0
        while queue:
            level_size = len(queue)
            height += 1
            for _ in range(level_size):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return height
