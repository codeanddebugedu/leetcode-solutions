# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Time Complexity -> O(NxN) -> O(N^2)
"""
from typing import Optional


class Solution:
    def calculateHeight(self, root):
        if not root:
            return 0
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)
        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lHeight = self.calculateHeight(root.left)
        rHeight = self.calculateHeight(root.right)
        if abs(lHeight - rHeight) > 1:
            return False

        leftSide = self.isBalanced(root.left)
        rightSide = self.isBalanced(root.right)
        if not leftSide or not rightSide:
            return False
        return True
