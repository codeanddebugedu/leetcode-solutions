"""
Time Complexity: O(N) 
where N height. 

Space Complexity: O(N) 
where N height. 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def solve(self, node):
        if node == None:
            return 0
        leftHeight = self.solve(node.left)
        rightHeight = self.solve(node.right)
        return 1 + max(leftHeight, rightHeight)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)
