# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Time Complexity -> O(N)
Space Complexity -> O(N)
"""
from typing import Optional


class Solution:
    def calculateHeight(self, root):
        if not root:
            return 0
        leftHeight = self.calculateHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.calculateHeight(root.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ans = self.calculateHeight(root)
        if ans >= 0:
            return True
        return False
