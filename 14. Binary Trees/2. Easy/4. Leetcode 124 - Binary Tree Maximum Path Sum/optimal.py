# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    maxi = float("-inf")

    def findMaxPathSum(self, root):
        if not root:
            return 0
        leftPathSum = max(0, self.findMaxPathSum(root.left))
        rightPathSum = max(0, self.findMaxPathSum(root.right))

        self.maxi = max(self.maxi, leftPathSum + root.val + rightPathSum)
        return max(leftPathSum, rightPathSum) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMaxPathSum(root)
        return self.maxi
